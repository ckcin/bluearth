#! /usr/bin/env python

## @ author: N Carrasco

import config


###########################
if __name__ == "__main__":
    print "bluearth" 
    configuration = config.buildParser().parse_args()
    print configuration
