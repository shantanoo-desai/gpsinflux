import json
import os
from influxdb import InfluxDBClient

def connect_db():
    """Configure a Database using the configuration file"""
    conf_file_path = os.getcwd() + '/configuration.json'
    with open(conf_file_path, 'r') as conf:
        conf_data = json.load(conf)
    db_conf_info = conf_data['db']
    try:
        db = InfluxDBClient(host=db_conf_info['host'],
                            port=db_conf_info['port'],
                            database=db_conf_info['name'])
    except Exception as e:
        raise e
    return db
