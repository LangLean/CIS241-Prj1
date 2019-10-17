#!/bin/bash
declare -a parray=(64 128 256 512)
for i in "${parray[@]}" 
do
	python $1.py $i >> $1.out
	python $2.py $i >> $2.out
	python $3.py $i >> $3.out
done	
#echo test > $1.out
#echo test > $2.out
#echo test > $3.out


