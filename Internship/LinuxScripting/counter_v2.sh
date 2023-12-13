#!/bin/bash

f1="bashcrc"
f2="bashcrc.txt"
if [ -e "$f1" ] && [ -e "$f2" ]; then
	string="StrictHostKeyChecking"
	echo -e "=====Results for bashrc=====\n"
	grep -n "$string" "$f1"
	echo -e "\n=====Results for bashrc.txt=====\n"
	grep -n "$string" "$f2"
	c1=$(grep -c "$string" "$f1")
	c2=$(grep -c "$string" "$f2")
	ct=$(( c1 + c2 ))
	echo -e "\n=====Total occurrences=====\n $ct"
else
	echo No such files
fi
