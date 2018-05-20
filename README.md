GPSInflux
=========

A Rudimentary Library written in `Python3` which parses information from**Adafruit Ultimate GPS (MTK3339)** module and stores information in an `InfluxDB` database.

You will need `tmux` and `python3.x` on your system

Note
----

-	please change the path to the repository in the `GPSSession.sh`
-	make executable `tmux` script use `chmod +x GPSSession.sh`
-	execute using `./GPSSession.sh`

### Components

-	The Library sets `$GPGGA` and `$GPRMC` sentences in the GPS Module and stores the following parameters:

	-	Latitude
	-	Longitude
	-	Altitude
	-	Speed Over Ground

-	`conf.json` has basic information of setup of GPS and DB

	-	DB Name: `example`
		-	measurement: `gps`
		-	fields: `lat`, `lat_dir`, `lon`, `lon_dir`, `alt`, `spd_over_grnd`
	-	DB Port: **8086**

### Dependencies

-	Install Dependencies using : `pip3 install -r requirements.txt`
-	or use `pip3 install` with the following: - `pyserial` - `pynmea2` - `influxdb`

### ChangeLog

1.	pass all exceptions but log `ERROR` level exceptions in `/var/log/gps.log`
2.	Create `tmux` session with **ever-respawning** script
