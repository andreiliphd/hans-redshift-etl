# Hans - Redshift ETL

============

Redshift is highly performant and optimized SQL database with ability to scale.
Queries are optimized using AQUA algorithm.
Usage is simple. Simpler than Spark.

---

## Features
- Redshift support

---

## Setup
Clone this repo:
```
git@github.com:andreiliphd/hans-redshift-etl.git
```


---

## File structure
`create_tables.py` - script creating tables.

`etl.ipynb` - Jupyter Notebook for ETL and analytics.

`etl.py` - script to run ETL process.

`sql_queries.py` - queries to Redshift.

`README.md` - instruction for this project.

---


## Usage
Use the following command to execute queries on a cluster.

1) Create configuration file `dwh.cfg`.
```python
[CLUSTER]
HOST={database_host}
DB_NAME={database_name}
DB_USER={database_username}
DB_PASSWORD={database_password}
DB_PORT={database_port}

[IAM_ROLE]
ARN= {arn_aws_iam}

[S3]
LOG_DATA=s3://udacity-dend/log_data
LOG_JSONPATH=s3://udacity-dend/log_json_path.json
SONG_DATA=s3://udacity-dend/song_data
```
2) Create tables.
```shell
python create_tables.py
```
3) Load data to tables.
```shell
python etl.py
```

---

## Explanation
Usage of sort and distribution keys can increase performance of the queries. 
Although loading time would increase but queries speed increase significantly.
Star schema is used when designing a database.
Star schema is good for running analytics and requires less postprocessing steps
for further analysis in BI tools.

---

## License
This project is licensed under the terms of the **MIT** license.