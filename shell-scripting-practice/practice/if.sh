#!/bin/bash

read -p "enter a number : " number

if [ $number -gt 5 ];
then
    echo "the number is positive"
fi


read -p "ebter your age :" age
if [ $age -gt 18 ];
then 
    echo "you are eligible to vote"
    fi

read -p "enter password : " password
if [ $password == "linux" ];
then 
    echo "access granted"
fi

