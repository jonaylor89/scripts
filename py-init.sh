#!/usr/bin/env bash

if [ "$1" ]
then

  project=$1

  printf "[$project] creating project structure\n"

  # Make directory for python project
  mkdir $project

  # Go into the new directory
  cd $project
else 
  project="$(basename $PWD)"

  printf "[$project] initializing project\n"
fi

# Initialize git repository
if test $(which git); then
  printf "[$project] Initializing git repository\n"
  git init

  touch .gitignore
else 
  printf "[$project] git not installed on the system, skipping...\n"
fi

# Create source directory
mkdir src

# Add placeholder file to source with basic skeleton
touch src/main.py
printf "#!/usr/bin/env python3

def main():
    pass
          
if __name__ == '__main__':
    main()
      
        " > src/main.py

# Make README and populate it
touch README.md
echo "# $project" > README.md 

# Create setup file for distrobution
touch setup.py

# Create virtual environment
if test $(which pipenv); then
  printf "[$project] initializing virtual environment\n"
  pipenv --python 3.7
else 
  printf "[$project] pipenv not installed on the system, skipping...\n"
fi

if test $(which git); then
  git add .
  git commit -m "init"
fi

printf "\n[$project] \x1b[32msetup complete!\x1b[m\n"







