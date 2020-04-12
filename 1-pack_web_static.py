#!/usr/bin/python3
"""Fabric script that compress the contents of the web_static folder
of AirBnB_Clone repo
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Compress the contents of the web_static folder of AirBnB_Clone repo"""

    try:
        file_name = "versions/web_static_" +\
                    datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
        route_to_compress = "web_static"
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf {} {}".format(file_name, route_to_compress))
        return file_name
    except:
        return None
