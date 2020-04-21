#!/bin/bash
# prints the input
function create() {
 	cd
    python create.py $1
    cd /Users/your-Homedirectory/Downloads/Projects/$1
    git init
    git remote add origin https://github.com/USERNAME/$1.git #git@github.com:USERNAME/$1.git (SSH)
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}

