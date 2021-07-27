import re
import csv
import os
import sys

if len(sys.argv) > 1: #FILEPATH 안넣으면 에러처리
    file_path = sys.argv[1] # 첫 인자 가져옴
else:
    print("please input csv file_path.")
    sys.exit(1)

def write_to_file_from_list(filepath, to_csv_list):
    if os.path.isfile(filepath) == False: # 파일이 존재하지 않을때
        mod = 'w' # write mode
    else:
        mod = 'a' # append mode

    with open(filepath, mod, encoding='utf-8') as f: #파일을 열고, file이 없으면 새로 만듬
            writer = csv.writer(f)
            if os.stat(filepath).st_size == 0: # 파일에 아무 내용이 없을 때 
                writer.writerow(fields) # csv_file columns
            writer.writerow(to_csv_list) # db_bench 실행 결과 파싱한 list를  csv파일에 씀
    f.close()

# initialize variable
latency = 0 
ops = 0
throughput = 0

r = open("./final_result.txt",mode='r',encoding='utf-8') # final_result.txt를 가져와서 
fields = ['latency', 'ops/sec', 'throughput(MB/s)'] # csv파일의 columns list
regex = re.compile(r'\d+\.?\d+') # regular expression ./final_result.txt의 내용중에 숫자만 추출하는 코드
for i in range(5):
    oneline_result = r.readline() # final_result.txt를 한줄 읽어서 oneline_result에 저장 다음 반복에서는 다음줄로
    to_row = regex.findall(oneline_result) # 위 regex를 이용하여 추출한 숫자를 리스트로 만듦
    latency_, ops_, throughput_ = map(float, to_row) # 리스트를 분해해서 3개의 변수로 나눔

# db_bench  result add!
    latency += latency_
    ops += ops_
    throughput += throughput_

latency = round(latency / 5, 2)# 5개의 latency를 평균낸 값
ops = round(ops / 5, 2)# 5개의 ops를 평균낸 값
throughput = round(throughput / 5, 2)# 5개의 throughput을 평균낸 값

list_for_csv = [latency, ops, throughput] # 리스트로 만들어서 저장

write_to_file_from_list(file_path, list_for_csv) # write_to_file_from_list를 이용하여 위 리스트의 값을 file_path(csv file)에 씀



    
