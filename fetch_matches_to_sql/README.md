<<<<<<< HEAD
# League One ETL Pipeline
## Project Overview

This project is a daily ETL pipeline that fetches upcoming English League One fixtures from the TheSportsDB API and stores them in a SQLite database. The code is organized into separate folders: dags/ contains the Airflow DAG for scheduling and execution, etl/ holds the functions for extracting and transforming data, and data/ stores the SQLite database (league_one.db).

## ETL Process

The ETL process consists of three steps. First, match data is extracted from the API. Next, the data is transformed by selecting relevant fields such as teams, date, time, and venue, and a timestamp is added to track the last update. Finally, the transformed data is loaded into the database, with records inserted or updated based on a unique match ID to avoid duplicates.

## irflow and Docker

The pipeline runs as an Airflow DAG, scheduled to execute daily, but it can also be triggered manually via the Airflow UI. The environment is fully Dockerized using Docker Compose, which allows the project to run without requiring a local Airflow installation.

## Database and Usage

The database can be queried directly for analysis, visualization, or as a data source, and it updates automatically with each DAG run.

## Future Improvements

Currently, the pipeline focuses on upcoming fixtures only, but it can easily be extended to include historical data, league standings, match results, or additional leagues.
=======
# data-engineering-projects
Portfolio of data engineering.
>>>>>>> 0898d1d90b7d1b6c6170fc42af4d30f24415df33
