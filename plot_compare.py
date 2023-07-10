import json
import numpy as np
import matplotlib.pyplot as plt

with open('res_nomal.json', 'r') as file:
    data1 = []
    for line in file:
        line_data = json.loads(line)
        data1.append(line_data['latency'])

with open('res_stress.json', 'r') as file:
    data2 = []
    for line in file:
        line_data = json.loads(line)
        data2.append(line_data['latency'])

# 箱ひげ図を作成する
fig, ax = plt.subplots()

# データセット1の箱ひげ図を追加
ax.boxplot(data1, positions=[1], widths=0.6)

# データセット2の箱ひげ図を追加
ax.boxplot(data2, positions=[2], widths=0.6)

# 軸の設定
ax.set_xticks([1, 2])
ax.set_xticklabels(['nomal', 'stress'])
ax.set_xlabel('Dataset')
ax.set_ylabel('Latency')

# グラフのタイトルを設定する
plt.title('Comparison of Load Test Results')

# グラフを表示する
plt.show()
