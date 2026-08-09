#!/bin/bash
clear
echo "=========================="
echo "  Backup Utility Module"
echo "=========================="


read -p "enter directory name: " dir

if [ -d "$dir" ]
then 
    echo "directory found $dir"
    echo "creating backup directory"
    sleep 1s

    backup_name=backup_$(basename= "$dir")_$(date +%Y-%m-%d)
    
    mkdir -p "$backup_name" && cp -R "$dir"/* $backup_name
   
    read -p "want to compress the backup? [y/n] : " choice
    
    case "$choice" in
   
     Y/y)
        echo "compressing the backup.."
        sleep 1s
    tar -czvf backup_$dir_$(date +%Y-%m-%d).tar.gz backup_$dir_$(date +%Y-%m-%d) 
    echo "files copied"
    sort | wc -l ;;

    N/n)
        exit ;;
esac
else
    echo "directory not found"
fi

