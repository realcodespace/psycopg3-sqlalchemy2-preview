from alchemy import engine
from model import account_table, address_table
from sqlalchemy import text, func
from sqlalchemy.orm import Session


def explain_analyze(sql):
    with engine.connect() as conn:
        curs = conn.execute(text("EXPLAIN ANALYZE %s" % sql))
        return '\n'.join(r[0] for r in curs.fetchall())


def test_explain_analyze():
    account_cols = account_table.columns
    address_cols = address_table.columns

    session = Session(engine)

    q = session.query(
        account_table.join(
            address_table,
            account_cols['id'] == address_cols['account_id'])
        )\
        .order_by(func.random())\
        .limit(1)

    plan = explain_analyze(
        q.statement.compile(compile_kwargs={
            "literal_binds": True}))

    print(plan)


if __name__ == '__main__':
    test_explain_analyze()
