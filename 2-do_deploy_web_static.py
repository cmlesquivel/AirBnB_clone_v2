#!/usr/bin/python3
"""Fabric script that deploy archive web_static folder into the serves
"""

from fabric.api import *

env.hosts = ['34.74.191.2', '54.90.167.15']


def do_deploy(archive_path):
    """Function that does the deploy"""

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
