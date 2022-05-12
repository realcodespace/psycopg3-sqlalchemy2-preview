from sqlalchemy import text
from alchemy import engine
from contextlib import closing, contextmanager
import psycopg


@contextmanager
def cleanup_raw(conn, autocommit=False):
    try:
        yield conn
        if autocommit:
            conn.commit()
    finally:
        conn.close()


sql_insert = """
    INSERT INTO address (id, line1, city, state, zip)
    VALUES (%s, '53 1st st', 'New York', 'NY', 10055)
"""

sql_delete = """
    DELETE FROM address WHERE id = %s
"""


def test_autocommit():

    with cleanup_raw(engine.raw_connection(), autocommit=False) as conn:
        conn.execute(sql_insert, (2000,))

    with cleanup_raw(engine.raw_connection(), autocommit=True) as conn:
        conn.execute(sql_insert, (2000,))

    with cleanup_raw(engine.raw_connection(), autocommit=True) as conn:
        try:
            conn.execute(sql_insert, (2000,))
        except psycopg.errors.UniqueViolation:
            print("Tests pass")

    with cleanup_raw(engine.raw_connection(), autocommit=True) as conn:
        conn.execute(sql_delete, (2000,))

if __name__ == '__main__':
    test_autocommit()