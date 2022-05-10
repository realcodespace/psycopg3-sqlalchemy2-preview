from contextlib import closing, contextmanager
from alchemy import engine, async_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, text, select
from model import account_table, address_table
from sql import account_city_qry
from datetime import datetime
import sys
import asyncio


async def async_query():
    async with async_engine.connect() as conn:
        res = await conn.execute(text(account_city_qry))
        return (datetime.now(), res.fetchone())


account_cols = account_table.columns
address_cols = address_table.columns

query = select(
    account_table.join(
        address_table,
        account_cols['id'] == address_cols['account_id'])
    )\
    .order_by(func.random())\
    .limit(1)

columns = ['id', 'first_name', 'last_name', 'city']


async def async_orm_query():
    async with AsyncSession(async_engine) as session:
        result = await session.execute(query)
        row = result.fetchone()
        return (datetime.now(), [row._mapping[col] for col in columns])


async def run_tasks(cb=async_query):
    n_tasks = 5
    results = await asyncio.gather(*[cb() for i in range(n_tasks)])
    most_recent = sorted(results, key=lambda x: x[0])
    for i, (date, result) in enumerate(most_recent):
        print(f'Task{i+1} finished at {date}')
        print(result)


if __name__ == '__main__':
    print('Asyncio with SQL')
    asyncio.run(run_tasks())
    print('Asyncio with ORM')
    asyncio.run(run_tasks(cb=async_orm_query))
