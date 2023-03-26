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
import httpx
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def getTelecodeByName(name):
    with open('stations.json', 'r', encoding='utf-8') as f:
        stations = json.load(f)
        
    for station in stations:
        if station['name'] == name:
            return station['teleCode']
    return None


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
        return None

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
        return None



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

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=5555)