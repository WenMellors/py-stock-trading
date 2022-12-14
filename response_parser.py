from Kline import Kline


def parse_kline_data(kline_data):
    """
    :param kline_data: K线请求拿到的 response 数据
    :return: Kline 对象列表（按时间顺序）
    """
    # 进行一些接口检查，以防接口变动
    assert kline_data['column'][0] == 'timestamp'
    assert kline_data['column'][2] == 'open'
    res = []
    for item in kline_data['item']:
        new_kline = Kline(open_p=item[2], high_p=item[3], low_p=item[4], close_p=item[5],
                          change_range=item[7])
        res.append(new_kline)
    return res
