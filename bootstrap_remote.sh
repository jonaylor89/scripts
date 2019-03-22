#!/usr/bin/env bash

repo=$1
token=""

test -z $repo_name && echo "Repo name required" 1>&2 && exit 1

curl -H "Content-Type:application/json" https://gitlab.com/api/v3/projects?private_token=$token -d "{ \"name\": \"$repo\" }"
