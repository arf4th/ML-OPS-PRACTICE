#!bin/bash

file=$1


check_file() {
    if [ -e $file ];
    then 
    echo "file exist"
    else 
   echo "file does not exist"
fi
}

show_size() {
    if [ -e $file ];
    then 
    size=$(du -h $file | cut -f1)
    echo "size of file is $size"
 else
    echo "file does not exist"
    fi
}

delete_file() {
    if [ -e $file ];
    then 
    rm -fr "$file"
    echo "file removed successfully"
     else
    echo "file does not exist"
    fi
}

rename_file() {
    if [ -e $file ];
    then 
    read -p "enter new file name" newname
    mv "$file" "$newname"
    echo "file renamed successfully"
    else
    echo "file does not exist"
    fi
}



echo "========================="
echo "     file utility         "
echo "========================="

echo "1. check file"
echo "2. show file size"
echo "3. remove file"
echo "4. rename file"

read -p "choose a option number" choice

case "$choice" in 

1) 
    check_file
    ;;

2) 
    show_size
    ;;

3)
    delete_file
    ;;
4) 
    rename_file
    ;;

*) 
    echo "option is invalid please choose again"
    ;;


esac
