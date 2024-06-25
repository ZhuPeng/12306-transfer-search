'''
Author: Vincent Young
Date: 2023-03-26 19:38:14
LastEditors: Vincent Young
LastEditTime: 2023-03-26 23:07:23
FilePath: /12306-Schedule/station.py
Telegram: https://t.me/missuo

Copyright © 2023 by Vincent, All Rights Reserved. 
'''
#!/usr/bin/env python3

import json

with open('station_name.txt', 'r', encoding='utf-8') as fd:
	data = fd.read()

stations = data.split('@')[1:]

parsed_stations = []
for station in stations:
	parts = station.split('|')
	parsed_stations.append({
		'initialCode': parts[0].upper(),
		'name': parts[1].strip(),
		'teleCode': parts[2],
		'pinyin': parts[3].upper(),
		'pinyinShort': parts[4].upper()
	})

with open('stations.json', 'w', encoding='utf-8') as f:
	json.dump(parsed_stations, f, ensure_ascii=False, indent=4)
	
print("Writing is complete!")
