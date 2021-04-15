-- Global land temperature by city indexes

CREATE INDEX city_index ON globallandtemperaturesbycity (city);
CREATE INDEX country_index ON globallandtemperaturesbycity (country);
CREATE INDEX average_temp_index ON globallandtemperaturesbycity (average_temp);
CREATE INDEX dt_index ON globallandtemperaturesbycity (dt);

-- Global land temperature by country indexes

CREATE INDEX country_index_t2 ON globallandtemperaturesbycountry (country);
CREATE INDEX average_temp_index_t2 ON globallandtemperaturesbycountry (average_temp);
CREATE INDEX dt_index_t2 ON globallandtemperaturesbycountry (dt);

-- Global land temperature by major city indexes

CREATE INDEX city_index_t3 ON globallandtemperaturesbymajorcity (city);
CREATE INDEX country_index_t3 ON globallandtemperaturesbymajorcity (country);
CREATE INDEX average_temp_index_t3 ON globallandtemperaturesbymajorcity (average_temp);
CREATE INDEX dt_index_t3 ON globallandtemperaturesbymajorcity (dt);

-- Global land temperature by state indexes
CREATE INDEX state_index_t4 ON globallandtemperaturesbystate (the_state);
CREATE INDEX country_index_t4 ON globallandtemperaturesbystate (country);
CREATE INDEX average_temp_index_t4 ON globallandtemperaturesbystate (average_temp);
CREATE INDEX dt_index_t4 ON globallandtemperaturesbystate (dt);

-- Global temperature indexes

CREATE INDEX dt_index_t5 ON globaltemperatures (dt);
