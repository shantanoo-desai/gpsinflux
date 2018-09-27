GPSInflux
=========

A Rudimentary Library written in `Python3` which parses information from**Adafruit Ultimate GPS (MTK3339)** module and stores information in an `InfluxDB` database.

-	You will need `python3.x` on your system.
-	`tmux` is good to have
-	`sudo` privileges if you need to use the Serial Port and log file to be saved in the `/var/log/` folder.

Note
----

If using the `tmux` script, do the following:

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
-	or use `virtualenv` as follows: $ virtualenv -p python3 env_test $ source env_test/bin/activate $ pip install .

ChangeLog
---------

### v1.0

1.	pass all exceptions but log `ERROR` level exceptions in `/var/log/gps.log`
2.	Create `tmux` session with **ever-respawning** script
3.	Add `setup.py`, `MANIFEST.in` for packaging purposes
4.	removed `status` measurement
