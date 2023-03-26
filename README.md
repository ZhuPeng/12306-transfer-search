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

## Author
**12305-Schedule** © [Vincent Young](https://github.com/missuo), Released under the [MIT](./LICENSE) License.<br>