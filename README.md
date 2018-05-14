GPSInflux
=========

A Rudimentary Library written in `Python3` which parses information from**Adafruit Ultimate GPS (MTK3339)** module and stores information in an `InfluxDB` database.

### Components

-	The Library sets `$GPGGA` and `$GPRMC` sentences in the GPS Module and stores the following parameters:

	-	Latitude
	-	Latitude Direction
	-	Longitude
	-	Longitude Direction
	-	Altitude
	-	Speed Over Ground

-	`configuration.json` has basic information of setup of GPS and DB

	-	DB Name: `example`
		-	measurement: `gps`
		-	fields: `lat`, `lat_dir`, `lon`, `lon_dir`, `alt`, `spd_over_grnd`
	-	DB Port: **8086**

### Dependencies

use `pip3 install` with the following: - `pyserial` - `pynmea2` - `influxdb`

### What it Lacks

-	proper `Exception` handling
-	Logging configuration
