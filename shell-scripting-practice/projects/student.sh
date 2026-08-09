#!/bin/bash


add_student() {
    read -p "enter your name : " name 
    read -p "enter your marks : " marks
}

display_student() {
    echo "student name is : $name"
    echo "student marks are : $marks"
}

calculate_average() {
    average=$marks
    echo "average marks : $average"
}

display_grade() {
    if [ "$average" -ge "90" ];
    then
    echo "grade A"
    elif [ "$average" -ge "70" ];
    then 
    echo "grade B"
    elif [ "$average" -ge "50" ];
    then 
    echo "grade C"
    else
    echo "YOU ARE FAIL!!!!"
    fi
}

add_student
display_student
calculate_average
display_grade