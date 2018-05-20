import json
import os
from influxdb import InfluxDBClient
import logging

logger = logging.getLogger("influxdb")
logger.setLevel(logging.ERROR)

handler = logging.FileHandler("/var/log/gps.log")
handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def connect_db():
    """Configure a Database using the configuration file"""
    conf_file_path = os.getcwd() + '/conf.json'
    with open(conf_file_path, 'r') as conf:
        conf_data = json.load(conf)
    logger.info('DB from Conf. Loaded')
    db_conf_info = conf_data['db']
    logger.debug(db_conf_info)

    try:
        db = InfluxDBClient(host=db_conf_info['host'],
                            port=db_conf_info['port'],
                            database=db_conf_info['name'])
    except Exception as e:
        logger.exception(e)
        pass
    return db
