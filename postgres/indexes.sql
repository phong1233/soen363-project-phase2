-- Global land temperature by city indexes

CREATE INDEX city_index ON globallandtemperaturesbycity (city);
CREATE INDEX country_index ON globallandtemperaturesbycity (country);
CREATE INDEX average_temp_index ON globallandtemperaturesbycity (average_temp);
CREATE INDEX dt_index ON globallandtemperaturesbycity (dt);

-- Global land temperature by country indexes

CREATE INDEX country_index ON globallandtemperaturesbycountry (country);
CREATE INDEX average_temp_index ON globallandtemperaturesbycountry (average_temp);
CREATE INDEX dt_index ON globallandtemperaturesbycountry (dt);

-- Global land temperature by major city indexes

CREATE INDEX city_index ON globallandtemperaturesbymajorcity (city);
CREATE INDEX country_index ON globallandtemperaturesbymajorcity (country);
CREATE INDEX average_temp_index ON globallandtemperaturesbymajorcity (average_temp);
CREATE INDEX dt_index ON globallandtemperaturesbymajorcity (dt);

-- Global land temperature by state indexes
CREATE INDEX state_index ON globallandtemperaturesbystate (the_state);
CREATE INDEX country_index ON globallandtemperaturesbystate (country);
CREATE INDEX average_temp_index ON globallandtemperaturesbystate (average_temp);
CREATE INDEX dt_index ON globallandtemperaturesbystate (dt);

-- Global temperature indexes

CREATE INDEX dt_index ON globaltemperatures (dt);
