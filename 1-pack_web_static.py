#!/usr/bin/python3
"""
    Generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

def do_pack():
     """Function to compress files"""
    from fabric.operations import local
    from datetime import datetime

    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None

if __name__ == "__main__":
    do_pack()
