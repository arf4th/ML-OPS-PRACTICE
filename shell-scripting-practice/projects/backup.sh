#!/bin/bash

read -p "Enter directory which you want to backup - " dir

if [ ! -d "$dir" ]
then
    echo "Directory does not exist"
    exit 1
fi

date=$(date +%Y-%m-%d)

backup="$dir/backup_$date"

mkdir -p "$backup"

count=0

for file in "$dir"/*
do
    if [ -f "$file" ]
    then
        if cp "$file" "$backup/"
        then
            ((count++))
        fi
    fi
done

echo "======================="
echo "Backup completed successfully"
echo "Backup location: $backup"
echo "Files copied: $count"
echo "======================="