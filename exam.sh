#!/bin/bash

#매개변수 변경가능


while getopts b:d:v:k:f: flag
do
	case "${flag}" in
		b) BENCHMARKS=${OPTARG};;
		d) DISABLE_WAL=${OPTARG};;
		f) FILEPATH=${OPTARG};;
	esac
done

read -r -p "please enter value size separated by space: " -a arr

cat /dev/null > $FILEPATH

for value_size in "${arr[@]}"

do

cat /dev/null > final_result.txt

for number in {1..5}

do

./db_bench  --benchmarks="$BENCHMARKS" --disable_wal="$DISABLE_WAL" --value_size="$value_size" > my_result.txt

sed -n '22p' my_result.txt >> final_result.txt

done

python3 test_pasing.py $FILEPATH

done

exit 0
