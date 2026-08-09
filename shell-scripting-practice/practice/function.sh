#!/bin/bash


welcome() {

    echo "Welcome to shell scripting"
}

welcome
welcome

#creating calculator using functions

#variables 
num1=10
num2=35


addition() {
    echo "addtion = $(($num1 + $num2))"
}

substraction() {
    echo "substraction = $(($num1 - $num2))"
}

multiplication() {
    echo "multuiplication = $(($num1 * $num2))"
}

division() {
    echo "division = $(($num1 / $num2))"
}

addition
substraction
multiplication
division

read -p "Enter you name : " name

output() {
    echo "Hello $name "
}
output



read -p "Enter first number : " first 
read -p "Enter second number : " second

largest() {
    if [ $first -gt $second ];
    then 
    echo "largest number : $first"
    else 
    echo "second number : $second"
    fi
}

largest "$num1" "$num2"

