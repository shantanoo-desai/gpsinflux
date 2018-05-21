import serial
import pynmea2
import time
import datetime
import logging
from gpsinflux.mtk3339 import mt3339
from gpsinflux.db import connect_db

logger = logging.getLogger("gpsFile")
logger.setLevel(logging.ERROR)

handler = logging.FileHandler("/var/log/gps.log")
handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def write_serial(serialport):
    """
    Write to the GPS Module. Currently display only GGA, RMC Messages at 1sec
    """
    logger.info('opening serial port')
    gps = mt3339(serialport)
    gps.set_nmea_output(gll = 0, rmc = 3, vtg = 0, gga = 3, gsa = 0, gsv = 0)
    gps.set_nmea_update_rate(1000)

def read_and_parse(serialport, baudrate, status = 0):
    """
    Read the GPS sentences and parse them to:
    Longitude, Longitude Degree
    Latitude, Latitude Degree
    Altitude, Altitude_Unit
    Speed Over Ground, Knots
    """
    logger.info('connect to DB')
    try:
        client = connect_db()
    except Exception as e:
        logger.error(e)

    com = None
    reader = pynmea2.NMEAStreamReader(errors='ignore')
    while True:
        if com is None:
            try:
                com = serial.Serial(serialport, baudrate, timeout=5.0)
            except serial.SerialException:
                logger.error('could not connect to %s' % serialport)
                time.sleep(5.0)
                continue
        try:
            data = com.read(16).decode('utf-8')
        except Exception as e:
            logger.error(e)
            pass
        try:

            for msg in reader.next(data):
                measurements = {}
                dat = pynmea2.parse(str(msg).strip('\r\n'))
                if not (dat.latitude == 0.0 and dat.longitude == 0.0):
                    # If Latitude and Longitude are not 0.0
                    if isinstance(dat, pynmea2.GGA):
                        print('Latitude: {} {}, Longitude: {} {}, Altitude: {} {}'
                                .format(dat.latitude, dat.lat_dir,
                                        dat.longitude, dat.lon_dir,
                                        dat.altitude, dat.altitude_units))
                        measurements['lat'] = dat.latitude
                        # measurements['lat_dir'] = dat.lat_dir
                        measurements['lon'] = dat.longitude
                        # measurements['lon_dir'] = dat.lon_dir
                        measurements['alt'] = dat.altitude
                    if isinstance(dat, pynmea2.RMC):
                        # print('Speed Over Ground: {} Knots'.format(dat.spd_over_grnd))
                        measurements['lat'] = dat.latitude
                        # measurements['lat_dir'] = dat.lat_dir
                        measurements['lon'] = dat.longitude
                        # measurements['lon_dir'] = dat.lon_dir
                        measurements['spd_over_grnd'] = dat.spd_over_grnd
                    # print(measurements)
                    measurements['status'] = status
                    client.write_points([{
                            'measurement': 'gps',
                            'tags': {
                                'type': 'gps-adafruit',
                            },
                            'time': datetime.datetime.utcnow().isoformat('T') + 'Z',
                            'fields': measurements
                        }])
                else:
                    print('Location Values not available yet. Not writing to DB')
        except Exception as e:
            logger.error(e)
            pass
