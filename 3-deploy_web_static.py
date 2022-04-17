#!/usr/bin/python3
"""
A Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy
"""
from fabric.operations import local, run, put, env
from datetime import datetime
import os

env.hosts = ['35.237.142.70', '35.231.108.250']
env.user = 'ubuntu'

def do_pack():
    """ Function to compress files in an archive """
    name = "versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None

def do_deploy(archive_path):
    """ function to dist to web server """
    if not os.path.exists(archive_path):
        return False
    if not put(archive_path, "/tmp/").succeeded:
        return False
    filename = archive_path[9:]
    foldername = "/data/web_static/releases/" + filename[:-4]
    filename = "/tmp/" + filename
    if not run('mkdir -p {}'.format(foldername)).succeeded:
        return False
    if not run('tar -xzf {} -C {}'.format(filename, foldername)).succeeded:
        return False
    if not run('rm {}'.format(filename)).succeeded:
        return False
    if not run('mv {}/web_static/* {}'.format(foldername,
                                              foldername)).succeeded:
        return False
    if not run('rm -rf {}/web_static'.format(foldername)).succeeded:
        return False
    if not run('rm -rf /data/web_static/current').succeeded:
        return False
    return run('ln -s {} /data/web_static/current'.format(
        foldername)).succeeded


def deploy():
    """ function to deploy """
    dep = do_pack()
    if dep is False:
        return False
    return do_deploy(dep)

if __name__ == "__main__":
    do_deploy()
