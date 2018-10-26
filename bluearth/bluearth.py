#! /usr/bin/env python

## @ author: N Carrasco

import config, imagery, wallpaper
from daemon import Daemon
import os, time

PID=os.path.dirname(os.path.realpath(__file__))+".bluearth.pid"

def log(level=False,msg=None):
    if level and msg is not None:
        print msg

# daemon class for running bluearth
class bluearthd(Daemon):
    def setConfig(self, config=None):
        if config is None:
            raise Exception("no configuration provided")
        config = config

    def run(self):
        print "I'm running with config: ",config
        while config.daemon or 1:
            # sleep then run
            if config.daemon: time.sleep(config.refresh*60.0)

            # get imagery
            log(config.verbose,"retrieving image from "+(config.url or imagery.imagery_urls[config.image]))
            image = imagery.getImage(url=config.url or imagery.imagery_urls[config.image],
                                 folder=config.storage)
            log(config.verbose,"image retrieved. written to: "+image)

            # set wallpaper
            log(config.verbose,"setting wallpaper")
            wallpaper.set_wallpaper(image)

            # break if not in daemon mode
            if not config.daemon: break

###########################
if __name__ == "__main__":
    config = config.buildParser().parse_args()
    log(config.verbose, config)

    bluearth = bluearthd(config.pid or PID)
    bluearth.setConfig(config)

    if config.daemon:
        bluearth.start()
    else:
        bluearth.run()

