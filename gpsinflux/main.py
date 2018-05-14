import json
import os
from gpsinflux.gps import read_and_parse, write_serial

def main():

    conf_file_path = os.getcwd() + '/configuration.json'
    with open(conf_file_path, 'r') as conf:
        conf_data = json.load(conf)
    db_conf_info = conf_data['gps']

    serialport = db_conf_info['serialport']
    baudrate = db_conf_info['baudrate']
    try:
        write_serial(serialport)
        read_and_parse(serialport, baudrate)
    except Exception as e:
        raise e
