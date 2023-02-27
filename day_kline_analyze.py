# 爬取股票的短期 K 线图（日图），并进行匹配是否出现特定的模式
import akshare
import json
from datetime import datetime, timedelta

with open('./data/my_stock_follows.json', 'r') as f:
    my_stock_dict = json.load(f)

# 参数控制
time_window_size = 100 # 因为 k 线分析都是比较近的数据分析，感觉不用爬取很远的数据

stock_code = '603799'
# 定义爬取的时间窗口，[start, end]
end_datetime = datetime.now()
end_date = end_datetime.strftime('%Y%m%d')
start_datetime = end_datetime - timedelta(days=time_window_size)
start_date = start_datetime.strftime('%Y%m%d')
# 这里我们使用前复权（因为 k 线分析主要是看盘）
stock_data_hist = akshare.stock_zh_a_hist(symbol=stock_code, period='daily', start_date=start_date, end_date=end_date,
                                          adjust='qfq')
stock_data_hist['MA5'] = stock_data_hist['收盘'].rolling(5).mean()
stock_data_hist['MA10'] = stock_data_hist['收盘'].rolling(10).mean()
stock_data_hist['MA20'] = stock_data_hist['收盘'].rolling(20).mean()

# 这里我们需要先判断当前股价的大体走势，是在上升期还是下降期

# 解析请求到的 k 线数据
kline_list = parse_kline_data(k_line_data)

# 这里还是维护一个变量吧，不然不好可能后续不好处理
# 但其实也可以加载一个预训练语料库，把中文转成嵌入向量（因为命名包含了正负情感？）
k_line_pattern = {
    '希望之星': 0,
    '反攻': 1,
    '曙光初现': 2,
    '旭日东升': 3,
    '平底': 4,
    '圆底': 5,
    '跳空三连阴': 6,
    '上升抵抗形': 7
}

signal_dict = {
    '见底信号': 0,
    '买进信号': 1,

}



def kline_pattern_match(data):
    """

    :param data: 历史 kline 数组
    :return: 匹配到的k线组合 string
    """
    # 判断一下是上涨周期，还是下跌周期
    # 就用均线来判断吧

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
    if (0 < data[-1].change_range < 1.5) and (0 < data[-2].change_range < 1.5) and \
            (0 < data[-2].change_range < 1.5) and (data[-1].high  > data[-2].high > data[-3].high):
        return '红三兵', '买进信号', '看涨'
    if (data[-1])

    # Default
    return '无模式', '无信号', '无'


print(kline_pattern_match(kline_list))
