#!/usr/bin/env python3

import os
import sys
import subprocess
from multiprocessing import Pool

def update_repo(repo):

    relative = repo.replace(os.environ['HOME'], '~')

    print("\n\x1b[95m=-=-=-=[{0}]=-=-=-=\x1b[m\n".format(relative))
    subprocess.run(['git', '--git-dir='+os.path.join(repo, '.git'),
                    'pull', 'origin', 'master']) 
    

if __name__ == '__main__':

    print("\n\x1b[32mPulling in later changes for all repositories...\x1b[m\n")

    default_path = os.path.join(os.environ['HOME'] + '/Repos')

    if len(sys.argv) < 2:
        repos = os.listdir(default_path)
        repos = [os.path.join(default_path, repo) for repo in repos if
                 os.path.isdir(os.path.join(default_path, repo))]
    else:
        repos = os.listdir(os.getcwd())
        repos = [os.path.join(os.getcwd(), repo) for repo in repos if
                 os.path.isdir(repo)]

    with Pool(10) as p:
        p.map(update_repo, repos)
    
    print("\n\x1b[32mComplete!\x1b[m\n")
