#!/bin/bash

skills=( "Python" "JavaScript" "Bash" "C++" "Java" )
for skill in "${skills[@]}"
do
echo "skill : $skill"
done


length=${#skills[*]}
echo "length of skills array : $length"