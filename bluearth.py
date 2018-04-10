#! /usr/bin/env python

## @ author: N Carrasco

import config, imagery, wallpaper


###########################
if __name__ == "__main__":
    print "bluearth" 
    config = config.buildParser().parse_args()
    print config

    # get imagery
    image = imagery.getImage(url=config.url or imagery.imagery_urls[config.image],
                             folder=config.storage)

    # set wallpaper
    wallpaper.set_wallpaper(image)
