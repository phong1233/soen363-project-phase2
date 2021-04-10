# Project Phase 2

## Objectives
* appreciating the powerof SQL in extracting and analyzing useful information from real datasets
* practicing andapplying the data systems concepts, mainly modeling, storing, and querying datasets on largedatasets
* appreciating the power of NoSQL in extracting and analyzing big datasets
* providing a comparison between SQL and NoSQL systems

## Dataset
[Climate Change: Earth Surface Temperature Data](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByMajorCity.csv)
## RDMS
* Postgres

### Getting started
* Install [docker](https://www.docker.com/)
* Extract the dataset in a root folder named **extracted**
* Run this command to start
    ```
    docker-compose up postgres
    ```
* Connect to:
    ```
    port = 5555
    db name = phase2
    user = postgres
    password = postgres
    ```
* To stop:
    ```
    docker-compose stop
    OR
    ctrl-c
    ```
* To re-run the init.sql stop the container and remove the db volume:
    ```
    sudo rm -rf ./postgres/db
    ```

## No SQL
* MongoDB

### Getting started
* Install [Mongo Compass](https://www.mongodb.com/products/compass)
* Install [docker](https://www.docker.com/)
* Run this command to start
    ```
    docker-compose up mongo
    ```
* Connect to:
    ```
    port = 27017
    user = mongo
    password = mongo
    ```
* To stop:
    ```
    docker-compose stop
    OR
    ctrl-c
    ```
* To delete database:
    ```
    sudo rm -rf ./mongo/db
    ```
* On mongo compass import the files:
    * listings.csv
    * reviews.csv
    * calendar.csv
* Don't forget to change the type of each columns