# Population scraping app

## Installing
```shell
git clone https://github.com/DSahalatyi/population_app
cd population_app
```

### <ins>.env file has been added for testing purposes and would normally be ignored</ins>

## Run with docker
### Configure .env file according to .env.example.

```shell
docker-compose up get_data
```
Parses the data from origin url and saves it to PostgreSQL.
```shell
docker-compose up print_data
```
Reads the data from PostgreSQL and prints it in the console in the next order

|Region|Total population| Biggest Country|Largest Population|Smallest Country|Smallest Population|
|---|---|--------------------------------|---|---|---|

## Features
- Asynchronous requests & database operations
- Ability to select between 2 origins by changing `DATA_ORIGIN` environmental variable
- Ability to print data in the form of table by changing `OUTPUT_FORMAT` environmental variable