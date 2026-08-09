#!/bin/bash

count=1 

for i in "$@"

do 
    echo "argument $count : $i"
    ((count++))
    done
    