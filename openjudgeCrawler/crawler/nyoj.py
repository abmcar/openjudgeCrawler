import re

import requests
import http.cookiejar as cookielib

from requests.cookies import cookiejar_from_dict

headers = {
    'GET' : '/userinfo/abmcar HTTP/1.1',
    'Host': 'nyoj.online',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    # 'sec-ch-ua': "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"
    # 'sec-ch-ua-mobile: ?0
    # 'sec-ch-ua-platform: "Windows"
    # 'Upgrade-Insecure-Requests: 1
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Sec-Fetch-Site: none
    # 'Sec-Fetch-Mode: navigate
    # 'Sec-Fetch-User: ?1
    # 'Sec-Fetch-Dest: document
    # 'Accept-Encoding: gzip, deflate, br
    # 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
    'Cookie': 'UM_distinctid=17c16d07e19d1d-0dd6ef3425ab05-57341f44-1fa400-17c16d07e1a41a; PHPSESSID=nq21coce16oe59kgrp3plc3dk3; CNZZDATA1273689806=1979339911-1632470151-%7C1632874968'

}


nowcookies = {
    'UM_distinctid': '17c16d07e19d1d-0dd6ef3425ab05-57341f44-1fa400-17c16d07e1a41a',
    'PHPSESSID' : 'nq21coce16oe59kgrp3plc3dk3',
    'CNZZDATA1273689806' : '1979339911-1632470151-%7C1632874968'
}

def request_dandan(url):
    try:
        s = requests.session()
        s.headers = headers
        # s.cookies = nowcookies
        # cookies = {}
        # cookie_str = 'UM_distinctid=17c16d07e19d1d-0dd6ef3425ab05-57341f44-1fa400-17c16d07e1a41a; PHPSESSID=nq21coce16oe59kgrp3plc3dk3; CNZZDATA1273689806=1979339911-1632470151-%7C1632874968'
        # for line in cookie_str.split(';'):
        #     key, value = line.split('=', 1)
        #     cookies[key] = value
        s.cookies = cookiejar_from_dict(nowcookies)
        # requests.utils.add_dict_to_cookiejar(s.cookies,{'CNZZDATA1273689806':'1979339911-1632470151-%7C1632874968'})
        # requests.utils.add_dict_to_cookiejar(s.cookies,{'PHPSESSID':'nq21coce16oe59kgrp3plc3dk3'})
        # requests.utils.add_dict_to_cookiejar(s.cookies,{'UM_distinctid':'17c16d07e19d1d-0dd6ef3425ab05-57341f44-1fa400-17c16d07e1a41a'})
        # nowCookie = cookielib.LWPCookieJar()
        # nowCookie = requests.
        # s.cookies.
        # now = Cookie()
        # s.cookies.set_cookie('CNZZDATA1273689806=1979339911-1632470151-%7C1632874968')
        # s.cookies.set_cookie()
        # s.cookies = {
        #     'CNZZDATA1273689806=1979339911-1632470151-%7C1632874968',
        #     'PHPSESSID=nq21coce16oe59kgrp3plc3dk3',
        #     'UM_distinctid=17c16d07e19d1d-0dd6ef3425ab05-57341f44-1fa400-17c16d07e1a41a'
        # }
        response = s.get(url=url, cookies=cookiejar_from_dict(nowcookies), headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


# <input type="text" id="ac_num" value="8" name="count_ac" class="layui-input" readonly="">

# def parse_result(html):
#     pattern = re.compile('<tr ><td>解决<td align=center><a href=.*?>(.*?)</a>', re.S)
#     # pattern = re.compile('<input type="text" id="ac_num" value=(.*?) name="count_ac" class="layui-input" readonly="">', re.S)
#     items = re.findall(pattern, html)
#     print(items)
#     return items[0]

def parse_result(html):
    pattern = re.compile('<tr ><td>解决<td align=center><a href=.*?>(.*?)</a>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    return items[0]


def get_solve_num(uid):
    url = 'https://nyoj.online/userinfo/' + str(uid)
    html = request_dandan(url)
    print(requests.get(url).text)
    items = parse_result(html)  # 解析过滤我们想要的信息
    # print(items)
    return int(items)


if __name__ == '__main__':
    print(get_solve_num('abmcar'))
