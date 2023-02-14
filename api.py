import requests
from datetime import datetime

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cookie': 'device_id=e6dc3c7bbe7af5f7402b9ab48112a099; s=cf11qbeoc3; acw_tc=2760826d16763829864831909e129a8b6044972cab66a85919a3e199fe1a68; Hm_lvt_1db88642e346389874251b5a1eded6e3=1676382987; xq_a_token=1e000a4b33b9fa6f26873d95e51f19861c6c615f; xqat=1e000a4b33b9fa6f26873d95e51f19861c6c615f; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjg2MTEzMTc0OTYsImlzcyI6InVjIiwiZXhwIjoxNjc4OTc1MDI2LCJjdG0iOjE2NzYzODMwMjY5NjMsImNpZCI6ImQ5ZDBuNEFadXAifQ.AWP9EusPwQkycPZygqWoi17y1TcDO6EtxvHeA2Ej35hMy97aGiYPYdSbMdG2lkaPjQTTwQbNFsVTtiTUI5iLl2eXdpCi_CitBAbdG-dFo9RR55L2QOPsUvHwPvoTcveQg7cvbDVHRLfGP3E5sMUuwUtakWOCIkcih0ioUiBp-Aai6I60dnLHFxms8y3ktHTiumuqFh6aCNWHKl264vHuDCI8xld-x9vSH5sqkebk3QbzVq0Af6oRQhZNr90VGgiob_3jE8wQzHBjvdgAhRfLp5myuRz3BLe-vOaveadPvLePjrhe0EJMD7Cz0VJSfG3wcVvrWoITUyS5jKP7oDWmsQ; xq_r_token=660bf710582cd0c58f57b689362e55193582e3cb; xq_is_login=1; u=8611317496; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1676383027; is_overseas=0'
}


# K 线图查询接口
def query_k_line(stock_code='SH603799', period='day'):
    stock_kline_api = 'https://stock.xueqiu.com/v5/stock/chart/kline.json'
    query_params = {
        'symbol': stock_code,
        'begin': int(datetime.now().timestamp()*1000),
        'period': period,
        'type': 'before',
        'count': '-284',  # 该参数控制查询距离 begin 多少天的 k 线数据
        'indicator': 'kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'
    }
    r = requests.get(stock_kline_api, headers=headers, params=query_params)
    if r.status_code != 200:
        raise Exception(r.content)
    return r.json()['data']
