import re
import csv
import numpy as np
import os
import sys

if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    print("please input csv file_path.")
    sys.exit(1)

def write_to_file_from_list(filepath, to_csv_list):
    if os.stat(filepath).st_size == 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            writer.writerow(to_csv_list)
    else:
        with open(filepath,'a',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(to_csv_list)
    f.close()

r = open("./final_result.txt",mode='r',encoding='utf-8')
fields = ['latency', 'ops/sec', 'throughput(MB/s)']
regex = re.compile(r'\d+\.?\d+')
for i in range(5):
    oneline_result = r.readline()
    to_row = regex.findall(oneline_result)
    latency_, ops_, throughput_ = map(float, to_row)

    if i == 0:
        latency = latency_
        ops = ops_
        throughput = throughput_
    if i != 0:
        latency += latency_
        ops += ops_
        throughput += throughput_

latency = latency / 5
ops = ops / 5
throughput = throughput / 5

list_for_csv = [latency, ops, throughput]

print(list_for_csv)
write_to_file_from_list(file_path, list_for_csv)



    
