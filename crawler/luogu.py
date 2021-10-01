import re

import requests


def request_dandan(url):
    try:
        s = requests.session()
        response = s.get(url=url)
        # print(response.text)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    if html is None:
        return 0
    # pattern = re.compile('<tr ><td>解决<td align=center><a href=.*?>(.*?)</a>', re.S)
    pattern = re.compile('已通过: (.*?)题', re.S)
    items = re.findall(pattern, html)
    # print(items)
    if len(items) == 0:
        return 0
    return items[0]


def get_solve_num(uid):
    url = 'https://luogu.wao3.cn/api/practice?id=' + uid
    html = request_dandan(url)
    # print(requests.get(url).text)
    items = parse_result(html)  # 解析过滤我们想要的信息
    return int(items)


# if __name__ == '__main__':
#     print(get_solve_num('54356'))
