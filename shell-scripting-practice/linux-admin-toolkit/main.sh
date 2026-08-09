#!/bin/bash

clear

while true
do 


echo "==============================="
echo "      Linux Admin Toolkit"
echo "==============================="


echo "1. System Information"
echo "2. File Management"
echo "3. Backup Utility"
echo "4. Process Monitor"
echo "5. Scheduler"
echo "6. Exit"


    read -p "Choose an option: " choice


case $choice in

1) 
    bash ./system_info.sh 
    ;;
2)
    bash ./file_manager.sh
    ;;
3)
    bash ./backup.sh
    ;;
4)
    bash ./process_monitor.sh
    ;;
5)
    bash ./schedular.sh
    ;;
6)
    echo "exiting linux admin toolkit..."
    exit 
    ;;
*)
    echo "Please choose valid option"
    ;;
esac

echo 
read -p "press enter to return the main menu"
clear
done