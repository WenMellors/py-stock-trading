# 爬取股票的短期 K 线图（日图），并进行匹配是否出现特定的模式
from api import query_k_line
from response_parser import parse_kline_data

stock_code = 'SH603799'

k_line_data = query_k_line(stock_code=stock_code, period='day')
# 解析请求到的 k 线数据
kline_list = parse_kline_data(k_line_data)


def kline_pattern_match(data):
    """

    :param data: 历史 kline 数组
    :return: 匹配到的k线组合 string
    """
    # if-else
    if data[-1].change_range > 0 and data[-2].mode == '十字星' and data[-3].change_range < 0:
        if data[-1].close > data[-3].close:
            # 希望之星
            return '希望之星', '见底信号', '看涨'
    else:
        return '无模式', '无信号', '无'


print(kline_pattern_match(kline_list))
