#!/bin/bash

read -p "enter a number : " number
if [ $number -gt 35 ];
then 
echo "pass"
else 
echo "fail"
fi

read -p "enter two numbers : " num1 num2
if [ $num1 -gt $num2 ];
then 
echo "first number is greater"
else 
echo "second number is greater"
fi

read -p "enter username : " username
if [ $username == "admin" ];
then 
echo "welcome administrator"
else
echo "access denied"
fi 
