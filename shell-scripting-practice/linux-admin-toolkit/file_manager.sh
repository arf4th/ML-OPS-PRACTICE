#!/bin/bash
clear
echo "=========================="
echo "  FILE MANAGEMENT MODULE"
echo "==========================="

echo "1. Check Whether a file exists"
echo "2. Show file size"
echo "3. Rename a file"
echo "4. Delete a file"
echo "5. Copy a file"
echo "6. Search text inside a file"
echo "7. Return to Main Menu"



read -p "select a option: " choice

case $choice in 

1) 
    
    read -p "enter file name: " search
    echo "Checking..."
    sleep 1s
    echo ""
    if [ -e $search ]
then 
    echo "File exist: $search"
else 
    echo "file does not exist"
fi
;;

2) 
    read -p "enter file name: " size
   echo "size of file is: $(du -h $size | awk '{print$1}')"
;;

3) 
    read -p "enter file name: " oldfile
    if [ -f $oldfile ]
then
     read -p "enter new file name: " rename
     mv $oldfile $rename
else
    echo "file does not exist" 
fi ;;

4) 
    read -p "enter file name: " delete
if [ -f $delete ]
then
    echo "deleting the file"
    rm $delete
    sleep 1s
    echo "successfully deleted the file"
else
    echo "File not found"
fi ;;

5) 
    read -p "enter file name: " copy
if [ -f $copy ]
then 
    read -p "enter the path where you want to copy the file: " path
    echo "copying file.."
    cp $copy $path
    sleep 1s
    echo "copied file succesfully into $path"
else 
    echo "file not found"
fi ;;
6)
    read -p "enter file name: " filename
if [ -f $filename ]
then
    read -p "enter text which you want to search" text
    grep $text $filename
else
    echo "file not found"
fi ;;
7)
    echo "exiting file manager..."
    exit ;;
esac
clear
echo ""