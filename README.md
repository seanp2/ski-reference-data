# ski-refernce-data
ski-reference-data is a repository for scripts involving database operations on the database powering [ski-reference.com](http://ski-reference.com/)

## Scripts

### run_upserter.sh
This script is used to pull data from a new FIS points list and upsert the data 
into the Athlete and Rankings tables in the production DB.

Required env vars:
- SKI_DB_PROD_USER 
- SKI_DB_PROD_PASSWORD 
- $SKI_DB_PROD_HOST 
- $SKI_DB_PROD_DB_NAME

```./run_upserter.sh PATH_TO_FIS_RANKING_CSV```

Example:

```./run_upserter.sh ~/Downloads/FIS-points-list-AL-2021-319.csv```



