# -*- coding: utf-8 -*-
"""
@Time        : 2021-09-07
@Author      : kunyuwan
@blog        :https://kunyuwan.github.io
@CSDN        :https://blog.csdn.net/qq_45740533
"""
import re

import requests


def request_dandan(url):
    try:
        s = requests.session()
        response = s.get(url=url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    if html is None:
        return 0
    # <tbody>.*?<tr>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td style="max-width: 200px;">.*?</td>.*?<td>(.*?)</td>.*?</tr>.*?</tbody>
    # pattern = re.compile('<tr ><td>解决<td align=center><a href=.*?>(.*?)</a>', re.S)
    pattern = re.compile('<tbody>.*?<tr>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td style="max-width: '
                         '200px;">.*?</td>.*?<td>(.*?)</td>.*?</tr>.*?</tbody>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    # print()
    if len(items) == 0:
        return 0
    return items[0]


def get_solve_num(uid):
    url = 'https://nyoj.online/ranklist?user_id=' + uid + '&nick='
    html = request_dandan(url)
    # print(requests.get(url).text)
    items = parse_result(html)  # 解析过滤我们想要的信息
    return int(items)


# if __name__ == '__main__':
#     print(get_solve_num('Abmcar'))
