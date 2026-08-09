#!/bin/bash


path="/d/shell scripting practice"
mkdir -p "$path/backup"

for file in "$path"/*.txt
do
    cp "$file" "$path/backup/"
    echo "$file copied"
done

echo "backup completed"