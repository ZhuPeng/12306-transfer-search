#!/usr/bin/env python3
import json
import httpx
import time

# curl https://kyfw.12306.cn/otn/resources/js/query/train_list.js > train_list.js
with open('train_list.js', 'r', encoding='utf-8') as fd:
	data = fd.read()

train_list = json.loads(data.split('=')[1].strip())
print(len(train_list))

trainNoDict = {}
parsed = []
max_date = ''
for k in train_list:
    if k > max_date:
        max_date = k
print('max_date:', max_date)
for tk, tv in train_list[max_date].items():
    print(tk, len(tv))
    for train in tv:
        traincode = train['station_train_code'] # Z1(北京西-长沙)
        no = train['train_no'] # 24000000Z10D
        trainNo = traincode.split('(')[0]
        item = {
            'trainNo': trainNo,
            'start': traincode.split('(')[1].split('-')[0].replace(' ', ''),
            'end': traincode.split('-')[1].split(')')[0].replace(' ', ''),
        }
        if trainNo in trainNoDict and trainNoDict[trainNo] != item:
            print(trainNo, 'already exits and not equal')
            print(trainNoDict[trainNo])
            print(item)
        parsed.append(item)
        trainNoDict[trainNo] = item

print('total:', len(parsed))
with open('train_list.json', 'w', encoding='utf-8') as f:
	json.dump(parsed, f, ensure_ascii=False, indent=4)
	
print("Writing is complete!")

cnt = 0
for t in parsed:
    print(t) # {'trainNo': 'D1954', 'start': '太原南', 'end': '重庆西'}
    for f in ['北京', '威海', '济南', '潍坊', '德州', '青岛']:
        if f in t['start']:
            r = httpx.get(url='http://127.0.0.1:5555/schedule?trainNo=' + t['trainNo'])
            if r.status_code != 200:
                print('404 => 403 exit')
                time.sleep(120)
            cnt += 1
            if cnt % 5 == 0:
                time.sleep(3)
