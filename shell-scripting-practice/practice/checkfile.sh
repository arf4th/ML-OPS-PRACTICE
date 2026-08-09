#!/bin/bash

for file in test{1..3}.txt
do 
touch $file
if [ -f $file ];
then 
echo "file $file exists"
else
echo "file not found"
fi
done
