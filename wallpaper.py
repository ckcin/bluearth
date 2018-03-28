#! /usr/bin/env python

## Module to set desktop wallpaper based on window manager
## @ author: N Carrasco

import os,sys
from subprocess import call


image_alpha = True


def get_manager():
    if "linux" not in sys.platform:
        raise Exception("Current implementation is Linux only")
    else:
        desktop_session = os.environ.get("DESKTOP_SESSION")
        if desktop_session in ["gnome","unity", "cinnamon", "mate", "xfce4", "lxde", "kde"] :
            return desktop_session

GSETTINGS_STRINGS = {
        "cinnamon" : "org.cinnamon.desktop.background",
        "gnome"    : "org.gnome.desktop.background",
        }

def set_wallpaper(image_file_with_path):
    setting_string = GSETTINGS_STRINGS[get_manager()]
    filepath = os.path.abspath(image_file_with_path)

    # works on Gnome3
    call(['gsettings', 'set', setting_string, 'picture-uri', 'file://%s' % (filepath)])
    return True



###########################
if __name__ == "__main__":
    print get_manager()
    set_wallpaper("/home/hcarrasc/opt/bluearth/imagery/current.jpg")
