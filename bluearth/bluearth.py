#! /usr/bin/env python

## @ author: N Carrasco

import config, imagery, wallpaper

# daemon class for running bluearth
class bluearthd():
    def __init__(self):
        print "do something daemony"

def log(level=False,msg=None):
    if level and msg is not None:
        print msg

###########################
if __name__ == "__main__":
    config = config.buildParser().parse_args()
    log(config.verbose, config)

    log(config.verbose,"retrieving image from "+(config.url or imagery.imagery_urls[config.image]))

    # get imagery
    image = imagery.getImage(url=config.url or imagery.imagery_urls[config.image],
                             folder=config.storage)

    log(config.verbose,"image retrieved. written to: "+image)

    # set wallpaper
    log(config.verbose,"setting wallpaper")
    wallpaper.set_wallpaper(image)
