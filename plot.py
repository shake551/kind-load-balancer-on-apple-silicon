import json
import matplotlib.pyplot as plt

# ファイルからVegetaの結果を読み取る
with open('res.json', 'r') as file:
    data = []
    for line in file:
        line_data = json.loads(line)
        data.append(line_data)

latencies = []
for item in data:
    latencies.append(item['latency'])

# 箱ひげ図を作成する
plt.boxplot(latencies)

# グラフのタイトルと軸ラベルを設定する
plt.title('Vegeta Load Test Results')
plt.xlabel('Measurement')

# グラフを表示する
plt.show()
