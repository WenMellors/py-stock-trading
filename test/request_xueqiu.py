import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cookie': 'device_id=e6dc3c7bbe7af5f7402b9ab48112a099; xq_is_login=1; u=8611317496; s=cf11qbeoc3; xq_a_token=a6973c642ef9492e87843f70598766bcedf86525; xqat=a6973c642ef9492e87843f70598766bcedf86525; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjg2MTEzMTc0OTYsImlzcyI6InVjIiwiZXhwIjoxNjczNDkxMTY4LCJjdG0iOjE2NzA4OTkxNjgxMDYsImNpZCI6ImQ5ZDBuNEFadXAifQ.FsjDbvmb5NKfvnvaKc9Lk79196V5HLcmIqcfu9kbaknJ1QzNCb1byuiKWL6c8scHQI7ZVaRUtIxopKCkfA79_9BtuXN3VqYfAP4fNCgK8zCbWPIy9WwQtgPhgEs9V9QWPKVETgucepGEuHvXRQPLuWSBQeIZfzSfB6QW1f8Q77tFHJbFx2JdrSR1iqNfEhdhQ3Zi1HopmT8lv-EW6B253tI5tnoBZ0p9HIOj0czASk2uMlM8PdPDesCKYHvRz2auTCD0y8JCtcN08zSVdRHbYeiJGTVkWp3YYpqV-Yk18Ef3NNgkhYz9kCySeCsdrZb5YmMjRoP5tra68H9gti4gOQ; xq_r_token=caf3d71d022644fb28033b036904587df86d867e; Hm_lvt_1db88642e346389874251b5a1eded6e3=1670858014,1670899169,1670985196,1671009279; snbim_minify=true; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1671009348'
}

r = requests.get('https://stock.xueqiu.com/v5/stock/chart/minute.json?symbol=SH603799&period=1d', headers=headers)
# 这是 ok 的，记得把代理关了
