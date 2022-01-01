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
git@github.com:andreiliphd/hans-redshift.git
```


---

## File structure
`create_tables.py` - script creating tables.

`etl.ipynb` - Jupyter Notebook for ETL and analytics.

`etl.py` - script to run ETL process.

`README.md` - instruction for this project.

---


## Usage
Use the following command to execute queries on a cluster.

1) Create tables.
```shell
python create_tables.py
```

2) Load data to tables.
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