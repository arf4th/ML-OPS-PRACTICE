#!/bin/bash


#basic while loop example

count=0
num=10

while [ $count -le $num ]
do 
echo " count is $count"
let count++
done

#user controlled loop

pass=linux123

while true
do 
read -p "enter your password" password

if [ "$password" == "$pass" ]
then 
echo "access granted"
break
else 
echo "password invalid"
fi 
done