# 定义 K 线对象，方便解析与计算

class Kline(object):
    """
    一个对象是一条k线
    """

    def __init__(self, open_p, high_p, low_p, close_p, change_range):
        """

        :param open_p: 开盘价
        :param high_p: 最高价
        :param low_p: 最低价
        :param close_p: 收盘价
        :param change_range: 涨跌幅度（百分比）
        """
        self.open = open_p
        self.high = high_p
        self.low = low_p
        self.close = close_p
        self.change_range = float(change_range)
        # 计算 k 线的阴阳
        if self.close < self.open:
            # 是一根阳线
            if self.change_range < 0.5:
                self.mode = '极阳'
            elif self.change_range < 1.5:
                self.mode = '小阳'
            elif self.change_range < 3.5:
                self.mode = '中阳'
            else:
                self.mode = '大阳'
        elif self.close > self.open:
            # 是一根阴线
            if self.change_range > -0.5:
                self.mode = '极阴'
            elif self.change_range > -1.5:
                self.mode = '小阴'
            elif self.change_range > -3.5:
                self.mode = '中阴'
            else:
                self.mode = '大阴'
        else:
            if self.high > self.low:
                self.mode = '十字星'
            else:
                self.mode = '平线'