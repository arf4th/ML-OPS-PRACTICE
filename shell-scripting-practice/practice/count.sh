#!/bin/bash

#path="/d/shell scripting practice"
for ls in "$path"
do 
ls "$ls"
echo "total files:" $(ls "$ls" | sort -n | wc -l)
done


while read myvar
do
wc -l
done <names.txt
