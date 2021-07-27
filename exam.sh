#!/bin/bash

#매개변수 변경가능


while getopts b:d:v:k:f: flag
do
	case "${flag}" in
		b) BENCHMARKS=${OPTARG};;
		d) DISABLE_WAL=${OPTARG};;
		f) FILEPATH=${OPTARG};; # FILEPATH의 이름은 아무거나 해도됨 파일이 없다면 자동으로 만들어짐
	esac
done

read -r -p "please enter value size separated by space: " -a arr # space마다 value_size가 arr에 들어감 ex) 16 100 200 arr = (16,100,200)

cat /dev/null > $FILEPATH # FILEPATH에 있는 내용을 삭제함

for value_size in "${arr[@]}" # arr에 있는 value_size를 하나씩 꺼냄

do

cat /dev/null > final_result.txt # 밑의 반복문이 반복될때 마다  final_result.txt를 지움 test_pasing에서는 

for number in {1..5} # 5번의 task case

do

./db_bench  --benchmarks="$BENCHMARKS" --disable_wal="$DISABLE_WAL" --value_size="$value_size" > my_result.txt # db_bench 실행

sed -n '22p' my_result.txt >> final_result.txt # my_result.txt의 22번째 줄의 내용을 final_result.txt에 저장

done

python3 test_pasing.py $FILEPATH # final_result.txt의 내용 중 성능 부분만 parsing하여 csv파일을 만듦

done

exit 0

# 끝
