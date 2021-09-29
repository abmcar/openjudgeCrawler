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
    # pattern = re.compile('<tr ><td>解决<td align=center><a href=.*?>(.*?)</a>', re.S)
    pattern = re.compile(
        '题已挑战</span>\n</div>\n<div class="my-state-item">\n<div class="state-num">(.*?)</div>\n<span>题已通过</span>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    return items[0]


def get_solve_num(uid):
    url = 'https://ac.nowcoder.com/acm/contest/profile/' + uid + '/practice-coding'
    # url = 'http://acm.zzuli.edu.cn/userinfo.php?user=' + uid
    html = request_dandan(url)
    # print(requests.get(url).text)
    items = parse_result(html)  # 解析过滤我们想要的信息
    # print(items)

    return int(items)


if __name__ == '__main__':
    print(get_solve_num('403376134'))
