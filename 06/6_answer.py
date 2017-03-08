import matplotlib.pyplot as plt
import numpy as np

data = np.load('6_data.npy') # データの読み込み
N = np.shape(data)[1] # データ数
K = 2 # クラスター（グループ）数
Iteration = 5 # パラメータ更新の繰り返し数
dot = ['or', 'xb'] # 各クラスタの点の見た目

# 初期代表点（適当に決めて構いません）
mu = np.array([[-0.9, 0.9], [0.9, -0.9]])

# 現在、i番目のデータが属する代表点（初期値0）
cluster = [0 for i in range(N)]

for n in range(Iteration):
    # データが属する代表点（cluster）を更新する
    for i in range(N):
        nearst = 10000 # 最も近い代表点との距離（初期値を10000とする）
        c = 0 # 最も近い代表点（初期値を0とする）
        for k in range(K):
            # ここまでで最も近い代表点との距離よりも
            # 近ければその点を最も近い代表点とする
            # np.linalg.norm(mu[k]-data[0:2,i:i+1])は2点の距離
            if nearst > np.linalg.norm(mu[k]-data[0:2,i]):
                nearst = np.linalg.norm(mu[k]-data[0:2,i])
                c = k
        # 最も近い代表点を現在の点iが属する代表点とする
        cluster[i] = c
    
    # 4章と同じ要領でクラスタごとにデータを分けます
    # ここではdatak[k]をk番目のクラスタのデータとします
    datak = [np.zeros((2, 1)) for k in range(K)]
    for i in range(N):
        datak[cluster[i]] = np.hstack((datak[cluster[i]], data[0:2, i:i+1]))
    # 最初の0を取り除きます
    for k in range(K):
        datak[k] = datak[k][0:2, 1:]
    
    # 現在のクラスタの重心を求め、代表点を更新します
    for k in range(K):
        x = float(np.average(datak[k][0]))
        y = float(np.average(datak[k][1]))
        mu[k] = x, y

# データ点をプロットする
# 4章と同じ要領でクラスタごとにデータを分けます
# ここではdatak[k]をk番目のクラスタのデータとします
datak = [np.zeros((2, 1)) for k in range(K)]
for i in range(N):
    datak[cluster[i]] = np.hstack((datak[cluster[i]], data[0:2, i:i+1]))

# 最初の0を取り除き、プロットします
for k in range(K):
    datak[k] = datak[k][0:2, 1:]
    plt.plot(datak[k][0], datak[k][1], dot[k])
    # 現在の代表点をプロットします
    plt.plot(mu[k][0], mu[k][1], 'sg')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('An example of k-means')
plt.savefig('kmeans.png')

    