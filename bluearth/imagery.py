#! /usr/bin/env python

## Module to retrieve and archive geostationary imagery
## @ author: N Carrasco

import os
import urllib
import datetime

imagery_urls = {
    "CONUS"  : "https://www.nnvl.noaa.gov/satimg/GERVISIR.JPG",
    "GOES_EAST"   : "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/latest.jpg",
    "GOES_WEST"   : "http://goes.gsfc.nasa.gov/goescolor/goeswest/pacific2/color_lrg/latest.jpg",
    "GLOBAL" : "https://static.die.net/earth/mercator/1600.jpg",
    "GOES16" : "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/latest.jpg",
    }

DEFAULT_URL  = imagery_urls["CONUS"]
DEFAULT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),"imagery")

def getLocation():
    # to eventually be developed to pull from system env
    return "GOES_EAST"

def getImage(url = DEFAULT_URL, folder = DEFAULT_PATH):
    if folder is None: folder = DEFAULT_PATH
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename=datetime.datetime.now().strftime("%Y%m%d%H%M")+".jpg"

    urllib.urlretrieve(url,os.path.join(folder,filename))

    #TODO: add check for file change
    #TODO: add option to purge older images

    currentfile=os.path.join(folder,"current.jpg")
    os.unlink(currentfile)
    os.symlink(filename,currentfile)

    return currentfile

def getLocaleImage(folder = DEFAULT_PATH):
    return getImage(imagery_urls[getLocation()], folder)
    
###########################
if __name__ == "__main__":
    getLocaleImage()

