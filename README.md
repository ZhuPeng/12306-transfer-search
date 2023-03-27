# 12306-Schedule
12306 Schedule API written in Flask

## User Guide
**You need to download the latest station information sheet by [following link](https://kyfw.12306.cn/otn/resources/js/framework/station_name.js).**
```
https://kyfw.12306.cn/otn/resources/js/framework/station_name.js
```

1. Parsing station information to JSON. Rename `station_name.js` to `station_name.txt`. Keep only the value and remove the variable name.
```shell
python3 station.py
```

2. Start installing the required environment.
```shell
pip3 install -r requirements.txt
```
3. Start Flask App.
```shell
python3 12306.py
```

4. Call the API.
```
# Query Train Info
[GET] http://example.com/info?trainNo=T212
or
[GET] http://example.com/info?trainNo=T212&date=20230326


# Query Train Schedule
[GET] http://example.com/schedule?trainNo=T212
or
[GET] http://example.com/schedule?trainNo=T212&date=20230326
```
**If no `date` parameter is passed, the time of the day is used by default.**

## Response Example
```json
{
  "data": {
    "date": "20230326",
    "from_station": "海拉尔",
    "station_train_code": "K996",
    "to_station": "成都西",
    "total_num": "44",
    "train_no": "050000K99610"
  }
}
```
```json
{
  "data": [
    {
      "arrive_time": "07:36",
      "end_station_name": "成都西",
      "isEnabled": true,
      "service_type": "1",
      "start_station_name": "海拉尔",
      "start_time": "07:36",
      "station_name": "海拉尔",
      "station_no": "01",
      "station_train_code": "K996",
      "stopover_time": "----",
      "train_class_name": "快速"
    },
    {
      "arrive_time": "08:30",
      "isEnabled": true,
      "start_time": "08:32",
      "station_name": "大雁",
      "station_no": "03",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "08:50",
      "isEnabled": true,
      "start_time": "08:55",
      "station_name": "牙克石",
      "station_no": "04",
      "stopover_time": "5分钟"
    },
    {
      "arrive_time": "09:20",
      "isEnabled": true,
      "start_time": "09:22",
      "station_name": "免渡河",
      "station_no": "05",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "09:46",
      "isEnabled": true,
      "start_time": "09:48",
      "station_name": "乌奴耳",
      "station_no": "06",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "10:42",
      "isEnabled": true,
      "start_time": "10:52",
      "station_name": "博克图",
      "station_no": "07",
      "stopover_time": "10分钟"
    },
    {
      "arrive_time": "11:37",
      "isEnabled": true,
      "start_time": "11:39",
      "station_name": "喇嘛山",
      "station_no": "08",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "11:51",
      "isEnabled": true,
      "start_time": "11:53",
      "station_name": "巴林",
      "station_no": "09",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "12:48",
      "isEnabled": true,
      "start_time": "12:51",
      "station_name": "扎兰屯",
      "station_no": "10",
      "stopover_time": "3分钟"
    },
    {
      "arrive_time": "13:56",
      "isEnabled": true,
      "start_time": "13:58",
      "station_name": "龙江",
      "station_no": "11",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "14:31",
      "isEnabled": true,
      "start_time": "14:33",
      "station_name": "富拉尔基",
      "station_no": "12",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "15:07",
      "isEnabled": true,
      "start_time": "15:32",
      "station_name": "齐齐哈尔",
      "station_no": "13",
      "stopover_time": "25分钟"
    },
    {
      "arrive_time": "16:24",
      "isEnabled": true,
      "start_time": "16:26",
      "station_name": "江桥",
      "station_no": "14",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "16:47",
      "isEnabled": true,
      "start_time": "16:49",
      "station_name": "平洋",
      "station_no": "15",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "17:13",
      "isEnabled": true,
      "start_time": "17:16",
      "station_name": "泰来",
      "station_no": "16",
      "stopover_time": "3分钟"
    },
    {
      "arrive_time": "18:00",
      "isEnabled": true,
      "start_time": "18:03",
      "station_name": "镇赉",
      "station_no": "17",
      "stopover_time": "3分钟"
    },
    {
      "arrive_time": "18:30",
      "isEnabled": true,
      "start_time": "18:43",
      "station_name": "白城",
      "station_no": "18",
      "stopover_time": "13分钟"
    },
    {
      "arrive_time": "19:08",
      "isEnabled": true,
      "start_time": "19:11",
      "station_name": "洮南",
      "station_no": "19",
      "stopover_time": "3分钟"
    },
    {
      "arrive_time": "20:29",
      "isEnabled": true,
      "start_time": "20:33",
      "station_name": "太平川",
      "station_no": "20",
      "stopover_time": "4分钟"
    },
    {
      "arrive_time": "21:15",
      "isEnabled": true,
      "start_time": "21:18",
      "station_name": "宝龙山",
      "station_no": "21",
      "stopover_time": "3分钟"
    },
    {
      "arrive_time": "22:11",
      "isEnabled": true,
      "start_time": "22:31",
      "station_name": "通辽",
      "station_no": "22",
      "stopover_time": "20分钟"
    },
    {
      "arrive_time": "23:47",
      "isEnabled": true,
      "start_time": "23:50",
      "station_name": "开鲁",
      "station_no": "23",
      "stopover_time": "3分钟"
    },
    {
      "arrive_time": "01:17",
      "isEnabled": true,
      "start_time": "01:19",
      "station_name": "查布嘎",
      "station_no": "24",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "02:12",
      "isEnabled": true,
      "start_time": "02:16",
      "station_name": "林东",
      "station_no": "25",
      "stopover_time": "4分钟"
    },
    {
      "arrive_time": "03:37",
      "isEnabled": true,
      "start_time": "03:58",
      "station_name": "大板",
      "station_no": "26",
      "stopover_time": "21分钟"
    },
    {
      "arrive_time": "05:00",
      "isEnabled": true,
      "start_time": "05:14",
      "station_name": "林西",
      "station_no": "27",
      "stopover_time": "14分钟"
    },
    {
      "arrive_time": "06:39",
      "isEnabled": true,
      "start_time": "06:41",
      "station_name": "经棚",
      "station_no": "28",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "08:36",
      "isEnabled": true,
      "start_time": "08:42",
      "station_name": "桑根达来",
      "station_no": "29",
      "stopover_time": "6分钟"
    },
    {
      "arrive_time": "09:54",
      "isEnabled": true,
      "start_time": "10:00",
      "station_name": "正镶白旗",
      "station_no": "30",
      "stopover_time": "6分钟"
    },
    {
      "arrive_time": "11:20",
      "isEnabled": true,
      "start_time": "11:22",
      "station_name": "化德",
      "station_no": "31",
      "stopover_time": "2分钟"
    },
    {
      "arrive_time": "13:18",
      "isEnabled": true,
      "start_time": "13:34",
      "station_name": "集宁南",
      "station_no": "32",
      "stopover_time": "16分钟"
    },
    {
      "arrive_time": "14:56",
      "isEnabled": true,
      "start_time": "15:16",
      "station_name": "呼和浩特东",
      "station_no": "33",
      "stopover_time": "20分钟"
    },
    {
      "arrive_time": "17:35",
      "isEnabled": true,
      "start_time": "17:55",
      "station_name": "包头",
      "station_no": "34",
      "stopover_time": "20分钟"
    },
    {
      "arrive_time": "19:21",
      "isEnabled": true,
      "start_time": "19:25",
      "station_name": "东胜西",
      "station_no": "35",
      "stopover_time": "4分钟"
    },
    {
      "arrive_time": "21:39",
      "isEnabled": true,
      "start_time": "21:47",
      "station_name": "榆林",
      "station_no": "36",
      "stopover_time": "8分钟"
    },
    {
      "arrive_time": "22:46",
      "isEnabled": true,
      "start_time": "22:53",
      "station_name": "绥德",
      "station_no": "37",
      "stopover_time": "7分钟"
    },
    {
      "arrive_time": "00:43",
      "isEnabled": true,
      "start_time": "00:47",
      "station_name": "延安",
      "station_no": "38",
      "stopover_time": "4分钟"
    },
    {
      "arrive_time": "06:25",
      "isEnabled": true,
      "start_time": "06:30",
      "station_name": "旬阳北",
      "station_no": "39",
      "stopover_time": "5分钟"
    },
    {
      "arrive_time": "07:11",
      "isEnabled": true,
      "start_time": "07:30",
      "station_name": "安康",
      "station_no": "40",
      "stopover_time": "19分钟"
    },
    {
      "arrive_time": "11:12",
      "isEnabled": true,
      "start_time": "11:20",
      "station_name": "达州",
      "station_no": "43",
      "stopover_time": "8分钟"
    },
    {
      "arrive_time": "12:24",
      "isEnabled": true,
      "start_time": "12:28",
      "station_name": "营山",
      "station_no": "44",
      "stopover_time": "4分钟"
    },
    {
      "arrive_time": "13:05",
      "isEnabled": true,
      "start_time": "13:09",
      "station_name": "南充",
      "station_no": "45",
      "stopover_time": "4分钟"
    },
    {
      "arrive_time": "13:54",
      "isEnabled": true,
      "start_time": "14:00",
      "station_name": "遂宁",
      "station_no": "47",
      "stopover_time": "6分钟"
    },
    {
      "arrive_time": "16:18",
      "isEnabled": true,
      "start_time": "16:18",
      "station_name": "成都西",
      "station_no": "48",
      "stopover_time": "----"
    }
  ]
}
```

## Author
**12306-Schedule** © [Vincent Young](https://github.com/missuo), Released under the [MIT](./LICENSE) License.<br>
