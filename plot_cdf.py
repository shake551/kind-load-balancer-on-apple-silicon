import json
import matplotlib.pyplot as plt
import numpy as np

# JSONファイルを読み取る
with open('res.json', 'r') as file:
    data = []
    for line in file:
        line_data = json.loads(line)
        data.append(line_data['latency'])

# レスポンス時間の配列を作成
response_times = []
for result in data:
    response_time = result / 1e6  # ナノ秒からミリ秒に変換
    response_times.append(response_time)

# レスポンス時間の配列をソート
sorted_response_times = np.sort(response_times)

# 累積分布関数（CDF）を計算
cdf = np.arange(1, len(sorted_response_times) + 1) / len(sorted_response_times)

# CDFをプロット
plt.plot(sorted_response_times, cdf, 'o', markersize=3)
plt.xlabel('Response Time (ms)')
plt.ylabel('CDF')
plt.title('Response Time CDF')
plt.grid(True)
plt.show()
