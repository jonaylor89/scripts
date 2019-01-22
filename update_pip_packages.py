#!/usr/bin/env python3

import pkg_resources
import subprocess
from multiprocessing import Pool


def update_package(package):

    print("\n\x1b[95m----------[{}]-----------\x1b[m\n".format(package))

    subprocess.call("pip install --upgrade " + package, shell=True)

if __name__ == '__main__':

    print("\n\x1b[32mUpdating all python3 pip packages\x1b[m\n")

    packages = [dist.project_name for dist in pkg_resources.working_set]

    with Pool(10) as p:
        p.map(update_package, packages)

    print("\n\x1b[32mComplete!\x1b[m\n")

