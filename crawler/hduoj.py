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
    pattern = re.compile('Accepted</td><td align=center>(.*?)</td>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    if len(items) == 0:
        return 0
    return items[0]


def get_solve_num(uid):
    url = 'http://acm.hdu.edu.cn/userstatus.php?user=' + uid
    html = request_dandan(url)
    # print(requests.get(url).text)
    items = parse_result(html)  # 解析过滤我们想要的信息
    return int(items)


if __name__ == '__main__':
    print(get_solve_num('abmcar'))
