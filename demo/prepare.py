from contextlib import closing
from alchemy import engine
from sql import account_city_qry


def prepare():
    with closing(engine.raw_connection()) as conn:
        curs = conn.execute(account_city_qry)
        print(conn)
        print("Prepare threshold: %s" % conn.prepare_threshold)

        print("Max prepared statements: %s" % conn.prepared_max)

        curs.execute(account_city_qry, prepare=True)
        print(curs, conn, conn.dbapi_connection, sep='\n')
        print(curs.fetchall())


if __name__ == '__main__':
    prepare()