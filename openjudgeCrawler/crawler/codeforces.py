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
    # pattern = re.compile('<tr ><td>解决<td align=center><a href=.*?>(.*?)</a>', re.S)
    pattern = re.compile('<div class="_UserActivityFrame_counterValue">(.*?) problems</div>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    if len(items) == 0:
        return 0
    return items[0]


def parse_rating(html):
    if html is None:
        return 0
    pattern = re.compile('<span style="font-weight:bold;" class=(.*?)>(.*?)</span> <span class="smaller"> \(max.',
                         re.S)
    items = re.findall(pattern, html)
    # print(items)
    if len(items) == 0:
        return 0
    return items[0][1]


def get_solve_num(uid):
    url = 'https://codeforces.com/profile/' + uid
    html = request_dandan(url)
    # print(requests.get(url).text)
    items = parse_result(html)  # 解析过滤我们想要的信息
    return int(items)


def get_rating(uid):
    url = 'https://codeforces.com/profile/' + uid
    html = request_dandan(url)
    # print(requests.get(url).text)
    items = parse_rating(html)  # 解析过滤我们想要的信息
    return int(items)

# if __name__ == '__main__':
#     print(get_rating('hesorchen'))
