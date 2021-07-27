#!/bin/bash

#매개변수 변경가능


while getopts b:d:v:k:f: flag
do
	case "${flag}" in
		b) BENCHMARKS=${OPTARG};;
		d) DISABLE_WAL=${OPTARG};;
		v) VALUE_SIZE=${OPTARG};;
		k) KEY_SIZE=${OPTARG};;
		f) FILEPATH=${OPTARG};;
	esac
done

cat /dev/null > $FILEPATH

for i in ${VALUE_SIZE}

do

cat /dev/null > final_result.txt

for number in {1..5}

do

./db_bench  --benchmarks="$BENCHMARKS" --disable_wal="$DISABLE_WAL" --value_size="$VALUE_SIZE" > my_result.txt

sed -n '22p' my_result.txt >> final_result.txt

done

python3 test_pasing.py $FILEPATH

done

exit 0
