#!/usr/bin/python3
"""Fabric script that creates and distributes an
archive to your web servers
"""
from fabric.api import *
from datetime import datetime
env.hosts = ['34.74.191.12', '54.90.167.155']


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


def do_deploy(archive_path):
    """Function that does the deploy into server"""

    if os.path.isfile(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")

        route = archive_path.split("/")

        file_name = route[len(route)-1].split(".")

        fname = file_name[0]

        route = "/data/web_static/releases/"

        sudo("mkdir -p {}{}".format(route, fname))

        run("sudo tar -C {}{} -xvzf /tmp/{}.tgz".format(route, fname, fname))

        sudo("rm /tmp/{}.tgz".format(fname))

        sudo("mv {}{}/web_static/* {}{}".format(route, fname, route, fname))

        sudo("rm -rf {}{}/web_static/ ".format(route, fname))

        sudo("rm /data/web_static/current")

        sudo("ln -sf {}{} /data/web_static/current".format(route, fname))

        return True

    except:
        return False


def deploy():
    """Call the functions do_pack and do_deploy"""

    archive_path = do_pack()
    if not archive_path:
        return False

    is_deploy = do_deploy(archive_path)
    return is_deploy
