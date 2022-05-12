# psycopg3-sqlalchemy2-preview

A thrilling psycopg3 tech preview with sqlalchemy

## Usage

```bash
# Build

docker-compose -f compose.yml build

# Run PostgreSQL

docker-compose -f compose.yml up -d

# Load tables with sample data

docker-compose -f compose.yml run app python demo/load_tables.py

# View a sample query plan

docker-compose -f compose.yml run app python demo/explain.py

# Test some async queries

docker-compose -f compose.yml run app python demo/async_query.py

# Prepared statements, cursors, _ConnectionFairy, dbapi_connection

docker-compose -f compose.yml run app python demo/prepare.py

# Autocommit with raw_connection()

docker-compose -f compose.yml run app python demo/autocommit.py

```

## References

https://www.psycopg.org/psycopg3/

https://docs.sqlalchemy.org/en/14/changelog/migration_20.html

https://github.com/sqlalchemy/sqlalchemy/issues/6842
