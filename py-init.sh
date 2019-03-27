#!/usr/bin/env bash

printf "[$1] create project structure\n"

# Make directory for python project
mkdir $1

# Go into the new directory
cd $1

# Initialize git repository
if test $(which git); then
  printf "[$1] Initializing git repository\n"
  git init

  touch .gitignore
else 
  printf "[$1] git not installed on the system, skipping...\n"
fi

# Create source directory
mkdir src

# Make README and populate it
touch README.md
echo "# $1" > README.md 

# Create setup file for distrobution
touch setup.py

# Create virtual environment
if test $(which pipenv); then
  printf "[$1] initializing virtual environment\n"
  pipenv --python 3.7
else 
  printf "[$1] pipenv not isntall on the system, skipping...\n"
fi







