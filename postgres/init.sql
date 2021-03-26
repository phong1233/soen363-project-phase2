CREATE TABLE GlobalLandTemperaturesByCity (
    dt DATE,
    average_temp REAL,
    average_temp_uncertainty REAL,
    city VARCHAR(50),
    country VARCHAR(50),
    longitude VARCHAR(20),
    latitude VARCHAR(20)
);

COPY GlobalLandTemperaturesByCity (dt, average_temp, average_temp_uncertainty, city, country, longitude, latitude)
FROM '/data/GlobalLandTemperaturesByCity.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE GlobalLandTemperaturesByCountry (
    dt DATE,
    average_temp REAL,
    average_temp_uncertainty REAL,
    country VARCHAR(50)
);

COPY GlobalLandTemperaturesByCountry (dt, average_temp, average_temp_uncertainty, country)
FROM '/data/GlobalLandTemperaturesByCountry.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE GlobalLandTemperaturesByMajorCity (
    dt DATE,
    average_temp REAL,
    average_temp_uncertainty REAL,
    city VARCHAR(50),
    country VARCHAR(50),
    longitude VARCHAR(20),
    latitude VARCHAR(20)
);

COPY GlobalLandTemperaturesByMajorCity (dt, average_temp, average_temp_uncertainty, city, country, longitude, latitude)
FROM '/data/GlobalLandTemperaturesByMajorCity.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE GlobalLandTemperaturesByState (
    dt DATE,
    average_temp REAL,
    average_temp_uncertainty REAL,
    the_state VARCHAR(50),
    country VARCHAR(50)
);

COPY GlobalLandTemperaturesByState (dt, average_temp, average_temp_uncertainty, the_state, country)
FROM '/data/GlobalLandTemperaturesByState.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE GlobalTemperatures (
    dt DATE,
    land_avg_temp REAL,
    land_avg_temp_uncertainty REAL,
    land_max_temp REAL,
    land_max_temp_uncertainty REAL,
    land_min_temp REAL,
    land_min_temp_uncertainty REAL,
    land_ocean_avg_temp REAL,
    land_ocean_avg_temp_Uncertainty REAL
);

COPY GlobalTemperatures (dt, land_avg_temp, land_avg_temp_uncertainty, land_max_temp, land_max_temp_uncertainty, land_min_temp, land_min_temp_uncertainty, land_ocean_avg_temp, land_ocean_avg_temp_Uncertainty)
FROM '/data/GlobalTemperatures.csv'
DELIMITER ','
CSV HEADER;
