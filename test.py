#!/usr/bin/env python3
import httpx

for s in [('北京', '青岛'), ('大明湖', '青岛'), ('大明湖', '淄博')]:
    url = 'http://127.0.0.1:5555/search?start=%s&end=%s&count=1' % (s[0], s[1])
    r = httpx.get(url=url).json()
    print(s, r)
    assert len(r['0-transfer']) > 0

for s in [('北京', '威海'), ('大明湖', '威海')]:
    url = 'http://127.0.0.1:5555/search?start=%s&end=%s&count=1' % (s[0], s[1])
    r = httpx.get(url=url).json()
    print(s, r)
    assert len(r['0-transfer']) == 0
    assert len(r['1-transfer']) > 0
