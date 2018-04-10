#! /usr/bin/env python

## Module for parsing configuration file 
## @ author: N Carrasco

import configargparse

def buildParser():
    parser = configargparse.ArgParser(default_config_files=['/etc/app/conf.d/*.conf', './bluearth.conf'],
                                      formatter_class=configargparse.ArgumentDefaultsHelpFormatter)
    parser.add('-c', '--config', is_config_file=True, help="path to local/override config file")
    parser.add('--url', help="url for retriving image",
               default=None)
    parser.add('--image', help="ALIAS for predefined image urls",
               choices=['CONUS','GOES_EAST','GOES_WEST','GLOBAL'],
               default='CONUS')
    parser.add('--refresh', help="Refresh rate (in minutes) for retreiving images in daemon mode",
            default=15)
    parser.add('--storage', help="Path to area to storge images",
               default=None)
    parser.add('--daemon', '-d', help="Run as daemon",
               action='store_true',
               default=False)
    parser.add('-v', '--verbose', help="verbose mode",
               action='store_true',
               default=False)

    return parser
