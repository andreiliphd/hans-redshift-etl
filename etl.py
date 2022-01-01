import configparser
import psycopg2
from sql_queries import loading_to_staging, insert_tables_to_production
import logging

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


def load_staging_tables(cur, conn):
    """
    Loading data into the staging tables from S3.
    """
    rootLogger.info("Loading staging tables.")
    for query in loading_to_staging:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Inserting data from staging tables to production tables.
    """
    rootLogger.info("Inserting data from staging tables in Star schema tables.")
    for query in insert_tables_to_production:
        cur.execute(query)
        conn.commit()


def main():
    """
    Performing followin actions:
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
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)
    conn.close()


if __name__ == "__main__":
    main()
