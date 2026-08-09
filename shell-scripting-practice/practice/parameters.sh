#!/bin/bash

#passing a name as parameter

greet() {
    echo "Hello $1"
}
greet "Arfath"

#passing a number

square() {
    echo "square = $1"
}
square "64"

area_rectangle()  {
    echo "area = $(($1 * $2))"
}
area_rectangle 60 100

student() {
    echo "Name : $1"
    echo "Age : $2"
    echo "Course : $3"
}
student "Arfath" "21" "BCA"


calculator() {

    case "$2" in
        +)
            echo "$(($1 + $3))"
            ;;
        -)
            echo "$(($1 - $3))"
            ;;
        \*)
            echo "$(($1 * $3))"
            ;;
        /)
            echo "$(($1 / $3))"
            ;;
    esac

}
calculator 10 + 10
calculator 20 - 10
calculator 2 * 2
calculator 100 / 400
