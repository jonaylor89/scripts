#!/usr/bin/env python3

import os
import sys
import subprocess
from multiprocessing import Pool

def listdirs(folder):
    for root, folders, files in os.walk(folder):
        for name in folders:
            yield root, name

def update_repo(repo):

    relative = repo.replace(os.environ['HOME'], '~')

    print("\n\x1b[95m=-=-=-=[{0}]=-=-=-=\x1b[m\n".format(relative))
    subprocess.run(['git', '--git-dir='+repo,
                    '--work-tree='+os.path.join(repo, '..'),
                    'pull', 'origin', 'master']) 
    

if __name__ == '__main__':

    print("\n\x1b[32mPulling in later changes for all repositories...\x1b[m\n")

    default_path = os.path.join(os.environ['HOME'] + '/Repos')

    if len(sys.argv) < 2:
        repos = [os.path.join(root, gitdir) for root, gitdir in
                 listdirs(default_path) if gitdir == ".git"]

    else:
        repos = [os.path.join(root, gitdir) for rot, gitdir in
                 listdirs(os.getcwd()) if gitdir == ".git"]

    with Pool(10) as p:
        p.map(update_repo, repos)
    
    print("\n\x1b[32mComplete!\x1b[m\n")
