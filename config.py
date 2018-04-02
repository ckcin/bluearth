#! /usr/bin/env python

## Module for parsing configuration file 
## @ author: N Carrasco

import configargparse

def buildParser():
    parser = configargparse.ArgParser(default_config_files=['/etc/app/conf.d/*.conf', './bluearth.conf'])
