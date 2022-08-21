#! usr/bin/bash

clear

center() {
  termwidth=$(stty size | cut -d" " -f2)
  padding="$(printf '%0.1s' ={1..500})"
  printf '%*.*s %s %*.*s\n' 0 "$(((termwidth-2-${#1})/2))" "$padding" "$1" 0 "$(((termwidth-1-${#1})/2))" "$padding"
}

echo -e "\033[92m"
echo
echo

center "STARING TO INSTALL DEPENDENCIES"
sleep 3

cod="\033[0m"
o="\033[91m"
grn="\033[92m"
blu="\033[34m"

cd $SCHOME

#Pillow Installatation
pkg install python3

pkg install git

pip install requests

python3 -m pip install --upgrade pip

clear
sleep 3

pip install requests

clear

sleep 1


echo -e "$blue HONGERA INSTALLATION COMPLITED"

clear

python3 start.py
