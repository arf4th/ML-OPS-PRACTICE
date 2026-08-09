#!/bin/bash

read -p"enter your marks : " marks
if [ $marks -ge 90 ];
then
echo "A"
elif [ $marks -ge 80 ];
then 
echo "B"
elif [ $marks -ge 70 ];
then 
echo "C"
elif [ $marks -ge 60 ];
then 
echo "D"
else [ $marks -le 60 ];
echo "Fail"
fi

read -p "enter a month number : " month
if [ $month -ge 10 ];
then 
echo "winter season"
elif [ $month -ge 6 ];
then 
echo "mansoon season"
elif [ $month -ge 3 ];
then 
echo "summer season"
else [ $month -le 2 ];
echo "winter season"
fi

read -p "enter salary amount : " salary
if [ $salary -ge 100000 ];
then 
echo "high salary"
elif [ $salary -ge 75000 ];
then 
echo "medium salary"
elif [ $salary -ge 50000 ];
then    
echo "low salary"
fi
