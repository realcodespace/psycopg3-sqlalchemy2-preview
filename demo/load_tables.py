from contextlib import closing
from sqlalchemy.orm import Session
from sqlalchemy import func
from alchemy import engine
from model import drop_all, create_all, account_table, address_table
import os


BLOCK_SIZE = 2 ** 10 * 4  # 4KB
BASEDIR = './data/'
account_csv_file = os.path.join(BASEDIR, 'account.csv')
address_csv_file = os.path.join(BASEDIR, 'address.csv')


def load_tables():
    with closing(engine.raw_connection()) as conn:
        with conn.cursor() as curs:
            with (open(account_csv_file, "r") as fh_account,
                  curs.copy("COPY account (id, first_name, last_name, email,\
                                           birth_date, locale)\
                            FROM STDIN") as copy_account):
                next(fh_account)  # Skip-header
                while data := fh_account.read(BLOCK_SIZE):
                    copy_account.write(data)
            with (open(address_csv_file, "r") as fh_address,
                  curs.copy("COPY address (line1, city, state, zip, account_id)\
                            FROM STDIN") as copy_address):
                next(fh_address)
                while data := fh_address.read(BLOCK_SIZE):
                    copy_address.write(data)
            conn.commit()


def test():
    session = Session(engine)
    assert session.scalar(
        func.count(account_table.columns['id'])) == 100
    assert session.scalar(
        func.count(address_table.columns['id'])) == 100
    print('Data load was successful')


if __name__ == '__main__':
    drop_all()
    create_all()
    load_tables()
    test()
