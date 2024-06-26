'''
Author: Vincent Young
Date: 2023-03-26 21:59:38
LastEditors: Vincent Young
LastEditTime: 2023-03-26 23:02:56
FilePath: /undefined/Users/vincent/Downloads/12306.py
Telegram: https://t.me/missuo

Copyright © 2023 by Vincent, All Rights Reserved. 
'''
#!/usr/bin/env python3

from flask import Flask, jsonify, request, abort
import json
import os
import httpx
import hashlib
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def load_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def listdir(dirname, prefix=''):
    files = [f for f in os.listdir(dirname) if not f.startswith('.')]
    if prefix != '':
        newfiles = []
        for f in files:
            if not f.startswith(prefix): continue
            newfiles.append(f)
        return newfiles
    return files

stations = load_json_file('stations.json')

def write_json_file(file, contents):
    with open(file, 'w', encoding='utf-8') as f:
	    json.dump(contents, f, ensure_ascii=False, indent=4)

def is_file_exists(p):
    if os.path.exists(p):
        return True
    return False

def cache_file(func):
    def wraper(*args, **kws):
        cfile = 'cache/' + func.__name__ + '-' + args[0]
        if is_file_exists(cfile):
            print('[HIT_CACHE] file:', cfile)
            return load_json_file(cfile)
        r = func(*args, **kws)
        if r is not None:
            write_json_file(cfile, r)
        return r
    return wraper

def getTelecodeByName(name):
    name = name.replace(' ', '')
    for station in stations:
        if station['name'] == name:
            return station['teleCode']
    return None

@cache_file
def queryTrainInfo(trainNo, date):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    url = "https://search.12306.cn/search/v1/train/search?keyword={}&date={}".format(
        trainNo, date)
    r = httpx.get(url=url, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        if "data" in data and len(data["data"]) > 0: 
            trainInfo = data["data"][0]
            return trainInfo
        else:
            return None
    else:
        print(r.status_code, r.text)
        return None

@cache_file
def queryTrainSchedule(trainNo, fromStation, toStation, date):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    url = "https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no={}&from_station_telecode={}&to_station_telecode={}&depart_date={}".format(
        trainNo, fromStation, toStation, date)
    r = httpx.get(url=url, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        if "data" in data and "data" in data["data"] and data["data"]["data"]:
            trainSchedule = data["data"]["data"]
            return trainSchedule
        else:
            return None
    else:
        print(r.status_code, r.text)
        return None

train_list = [load_json_file('cache/'+f) for f in listdir('cache/', prefix='queryTrainInfo-')]
for t in train_list:
    t['schedule'] = queryTrainSchedule(t['train_no'], '', '', '')

@app.route('/')
def hello():
    return jsonify({"message": "Hello!"})

@app.route('/info')
def info():
    trainNo = request.args.get('trainNo')
    date = request.args.get('date')
    if date is None:
        date = datetime.datetime.today().strftime('%Y%m%d')
    trainInfo = queryTrainInfo(trainNo, date)
    if trainInfo == None:
        abort(404)
    else:
        return jsonify(data = trainInfo)

@app.route('/schedule')
def schedule():
    trainNo = request.args.get('trainNo')
    date = request.args.get('date')
    if date is None:
        date = datetime.datetime.today().strftime('%Y%m%d')
    dateNew = f"{date[0:4]}-{date[4:6]}-{date[6:8]}"
    trainInfo = queryTrainInfo(trainNo, date)
    if trainInfo == None:
        abort(404)
    else: 
        newTrainNo = trainInfo["train_no"]
        fromStation = getTelecodeByName(trainInfo["from_station"])
        toStation = getTelecodeByName(trainInfo["to_station"])
        TrainSchedule = queryTrainSchedule(newTrainNo, fromStation, toStation, dateNew)
        if TrainSchedule == None:
            abort(404)
        else:
            return jsonify(data = TrainSchedule)

def get_match_train(name):
    r = []
    for t in train_list:
        if t['schedule'] is None:
            print(t)
            continue
        for idx, s in enumerate(t['schedule']):
            if name in s['station_name']: 
                r.append((idx, t))
                break
    return r

def get_full_match_train(start, end):
    r = []
    for t in train_list:
        if t['schedule'] is None:
            print(t)
            continue
        start_idx = -1
        for idx, s in enumerate(t['schedule']):
            if start in s['station_name']: 
                start_idx = idx
                break
        if start_idx == -1: continue

        end_idx = start_idx + 1
        while end_idx < len(t['schedule']):
            if end in t['schedule'][end_idx]['station_name']:
                break
            end_idx += 1
        if end_idx == len(t['schedule']): continue
        r.append(t)
    return r

def get_mins(t):
    a = [int(i) for i in t.split(':')]
    return a[0]*60 + a[1]

def time_diff_mins(start, end):
    start_mins = get_mins(start)
    end_mins = get_mins(end)
    return end_mins - start_mins

def is_time_in_range(t, trange):
    rstart = trange.split('-')[0]+':00'
    rend = trange.split('-')[1]+':00'

    return time_diff_mins(rstart, t) > 0 and time_diff_mins(t, rend) > 0

# downloads train list: https://github.com/FlyingRadish/12306-api
@app.route('/search')
def transfer_search():
    start = request.args.get('start')
    end = request.args.get('end')
    count = int(request.args.get('count', 1))
    transfer_time_min = int(request.args.get('transfer_time_min', 20))
    transfer_time_max = int(request.args.get('transfer_time_max', 120))
    start_time_range = request.args.get('start_time_range', '20-24')
    arrive_time_range = request.args.get('arrive_time_range', '5-12')
    match_train = get_full_match_train(start, end)
    res = {'args': request.args, '0-transfer': match_train}
    if count == 0:
        return jsonify(res)

    transfer = []
    start_match = get_match_train(start)
    for idx, m in start_match:
        transfer_idx = idx + 1
        while transfer_idx < len(m['schedule']):
            transfer_station = m['schedule'][transfer_idx]['station_name']
            trans_match = get_match_train(transfer_station)
            for tidx, tm in trans_match:
                end_tidx = tidx + 1
                while end_tidx < len(tm['schedule']):
                    end_station = tm['schedule'][end_tidx]['station_name']
                    if end not in end_station:
                        end_tidx += 1
                        continue
                    first_transfer = {
                        'start_idx': idx,
                        'start_station': m['schedule'][idx]['station_name'],
                        'start_time': m['schedule'][idx]['start_time'],
                        'end_idx': transfer_idx,
                        'end_station': transfer_station,
                        'arrive_time': m['schedule'][transfer_idx]['arrive_time'],
                        'train_info': m,
                    }
                    seccond_transfer = {
                        'start_idx': tidx,
                        'start_station': tm['schedule'][tidx]['station_name'],
                        'start_time': tm['schedule'][tidx]['start_time'],
                        'end_idx': end_tidx,
                        'end_station': end_station,
                        'arrive_time': tm['schedule'][end_tidx]['arrive_time'],
                        'train_info': tm,
                    }
                    diff = time_diff_mins(first_transfer['arrive_time'], seccond_transfer['start_time'])
                    if diff < transfer_time_min or diff > transfer_time_max or not is_time_in_range(first_transfer['start_time'], start_time_range) or not is_time_in_range(seccond_transfer['arrive_time'], arrive_time_range): 
                        print('[filter]:', '[first]-->', m, '[second]-->', tm)
                        end_tidx += 1
                        continue
                    transfer.append((first_transfer, seccond_transfer))
                    break
            transfer_idx += 1
    res['1-transfer'] = transfer
    return jsonify(res)

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.debug = True
    app.run(host='0.0.0.0', port=5555)
