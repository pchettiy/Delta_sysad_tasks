#!/bin/bash
for i in $(seq 1 100)
do
	mkdir folder_$i
	touch folder_$i/file_$i.txt
	chmod 700 folder_$i
done
