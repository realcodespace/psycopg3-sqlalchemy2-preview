from sqlalchemy import (
    Table, Column, String, MetaData,
    ForeignKey, Integer, Date)
from alchemy import engine
import sys


meta = MetaData()

account_table = Table(
    'account', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column('email', String, nullable=False),
    Column('birth_date', Date, nullable=False),
    Column('locale', String, nullable=False)
)

address_table = Table(
    'address', meta,
    Column('id', Integer, primary_key=True),
    Column('account_id', Integer, ForeignKey('account.id')),
    Column('line1', String, nullable=False),
    Column('city', String, nullable=False),
    Column('state', String),
    Column('zip', String, nullable=False)
)


def create_all():
    with engine.connect() as conn:
        with conn.begin():
            meta.create_all(conn)
        meta.reflect(conn)


def drop_all():
    with engine.connect() as conn:
        with conn.begin():
            meta.drop_all(conn)
        meta.reflect(conn)


if __name__ == '__main__':
    params = sys.argv[1:]
    if 'drop' in params:
        drop_all()
    else:
        create_all()
