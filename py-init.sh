#!/usr/bin/env bash

# Make directory for python project
mkdir $1

# Go into the new directory
cd $1

if test ! $(which git); then
  git init

  touch .gitignore
fi

# Create source directory
mkdir src

# Make README and populate it
touch README.md
echo "# $1" > README.md 

# Create setup file for distrobution
touch setup.py

if test ! $(which pipenv); then
  pipenv --python 3.7
fi







