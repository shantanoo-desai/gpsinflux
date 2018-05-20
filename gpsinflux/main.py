import json
import os
import logging
from gpsinflux.gps import read_and_parse, write_serial

logger = logging.getLogger("main")
logger.setLevel(logging.ERROR)

handler = logging.FileHandler("/var/log/gps.log")
handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def main():

    conf_file_path = os.getcwd() + '/conf.json'
    with open(conf_file_path, 'r') as conf:
        conf_data = json.load(conf)
    logger.info('got gps conf')
    db_conf_info = conf_data['gps']

    serialport = db_conf_info['serialport']
    baudrate = db_conf_info['baudrate']
    logger.info('setting RMC and GGA sentences')
    write_serial(serialport)
    logger.info('acquiring information')
    read_and_parse(serialport, baudrate)
