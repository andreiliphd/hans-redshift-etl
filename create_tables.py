import configparser
import psycopg2
from sql_queries import create_tables_in_database, drop_tables_in_database
import logging

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


def drop_tables(cur, conn):
    """
    Drop tables.
    """
    rootLogger.info("Dropping tables.")
    for query in drop_tables_in_database:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create tables.
    """
    rootLogger.info("Creating tables.")
    for query in create_tables_in_database:
        cur.execute(query)
        conn.commit()


def main():
    """
    Performing following actions:
    1.) Reading configuration file.
    2.) Connecting to database.
    3.) Executing queries.
    """
    rootLogger.info("Reading configuration files.")
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    rootLogger.info("Connecting to database.")
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
