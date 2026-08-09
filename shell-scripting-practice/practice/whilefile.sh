#!/bin/bash

while read myvar
do 
echo "Name: $myvar"
done <names.txt

path="/d/shell scripting practice"

echo "
admin
john
test
guest" > users.txt

read -p "enter username : " name
while read user
do
if [ "$name" == "$user" ];
then 
    echo "user exist"
    break
else
    echo "user not found"
fi
done < users.txt

