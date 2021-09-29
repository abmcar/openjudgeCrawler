import requests

headers = {
    'POST': '/v1/trace/Student/dailyreportadd HTTP/1.1',
    'Host': 'xg.nyist.vip',
    'Connection': 'keep-alive',
    'Content-Length': '88',
    'appid': '1',
    # 'Accept': 'application/json, text/plain, */*',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/x-www-form-urlencoded',
    'guest': 'b2w4YlB2elksMjA2MDksSk01WERuXzksMTYzMjgyNzQwNS45NjA4LDRwbUNGejh2Y3BTcyw4NmM1NDE1ZGI0OGNlYmIyNjJmYWExZWRmN2M3YTAyNA==',
    'token': '0c20b2b4-851b-40d4-b187-08e4ffb124a3',
    'Referer': 'https://servicewechat.com/wx5d22ba28f10a2e09/48/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br'

}

data = {
    'pcc': '410000,411300,411302',
    'gps': '33.0936,112.5996',
    'location': '2',
    'status': '0',
    'temp': '0',
    'contact': 0
}
r = requests.post('https://xg.nyist.vip/v1/trace/Student/dailyreportadd', params=headers, data=data)
print(r.status_code)
print(r.json())
print(r.headers)
