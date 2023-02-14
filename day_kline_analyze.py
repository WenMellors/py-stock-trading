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
    if data[-1].change_range > 0 and data[-2].change_range < 0:
        # 前阴，后阳
        if (data[-2].mode == '大阴' and data[-1].change_range >= 1.5) and \
                abs(data[-2].close - data[-1].close) / data[-2].close < 0.001:
            # 反攻信号
            return '反攻', '见底信号', '看涨'
        elif data[-2].change_range <= -1.5 and data[-1].change_range >= 1.5:
            if data[-1].open < data[-2].close and data[-1].close >= data[-2].middle:
                # 曙光初现
                return '曙光初现', '见底信号', '看涨'
            elif data[-1].open > data[-2].close and data[-1].close > data[-2].open:
                # 旭日东升
                return '旭日东升', '见底信号', '看涨'
        elif data[-2].low == data[-1].low:
            # 平底
            return '平底', '见底信号', '看涨'
    if data[-1].change_range >= 1.5:
        # 中阳或大阳
        # 这里是一个专门判断“圆底”模式的 code
        # 搜寻是否是前面一串小阳小阴，然后一根大阴
        # 感觉不能太多了吧，这里设置 step 为 6 (这样就已经是 7 个交易日了，已经很久了)
        i = len(data) - 2
        step = 6
        while i >= 0 and step > 0:
            if -1.5 < data[i].change_range < 1.5:
                # 是小阴或小阳
                i -= 1
                step -= 1
            elif data[i] <= -1.5 and step != 6:
                # 中阴或大阴
                return '圆底', '见底信号', '看涨'
            else:
                break
    if (data[-1].change_range < 0 and data[-1].open < data[-2].close) and \
            (data[-2].change_range < 0 and data[-2].open < data[-3].close) and \
            (data[-3].change_range < 0 and data[-3].open < data[-4].close):
        # 跳空三连阴
        return '跳空三连阴', '见底信号', '看涨'
    # Default
    return '无模式', '无信号', '无'


print(kline_pattern_match(kline_list))
