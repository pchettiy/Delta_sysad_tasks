#!/bin/bash
for i in $(seq 1 100)
do
mkdir folder_$i

touch file_$i.txt
mv file_$i.txt folder_$i

done
