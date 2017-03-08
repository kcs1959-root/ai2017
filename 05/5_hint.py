import matplotlib.pyplot as plt
import numpy as np

data = np.load('5_data.npy') # データの読み込み
N = np.shape(data)[1] # データ数
Iteration = 5 # パラメータ更新の繰り返し数

# データを2種類に分ける

# 以下で使われている、
# 最初に縦（または横）の大きさの1列（行）の0配列を作り、
# データをnp.hstack（またはnp.vstack）で加えてから最初の0を取り除く手法は
# よく使われるテクニックなので覚えておくと便利です
data0 = np.zeros((3, 1))
data1 = np.zeros((3, 1))

for i in range(N):
    # 3行目が-1か1かでdata0とdata1に分類
    if data[2][i] == -1:
        data0 = np.hstack((data0, data[0:3, i:i+1]))
    else:
        data1 = np.hstack((data1, data[0:3, i:i+1]))

# 最初の0を取り除きます
data0 = data0[0:3, 1:]
data1 = data1[0:3, 1:]

# データ点をプロットする
plt.figure()

plt.plot(data0[0], data0[1], 'or') # 赤色の丸点
plt.plot(data1[0], data1[1], 'xb') # 青色の罰点

# 各データの点の個数
N0 = np.shape(data0)[1] # data0の個数
N1 = np.shape(data1)[1] # data1の個数

# 初期値（適当に決めて構いません）
w0 = 0
w1 = -1
w2 = 1

# 式3.13〜3.15
for n in range(Iteration):
    # data0
    for i in range(N0):
        if # 書き込んでください  # 分類が誤っている点
            w0 += # 書き込んでください
            w1 += # 書き込んでください
            w2 += # 書き込んでください
    # data1
    for i in range(N1):
         if # 書き込んでください # 分類が誤っている点
            w0 += # 書き込んでください
            w1 += # 書き込んでください
            w2 += # 書き込んでください

# 求めた直線を描写します
# y = -(1/w2)(w0+w1*x)です
x = np.arange(-2, 2, 0.01)
y = -(1/w2) * (w0 + w1 * x)
plt.plot(x, y)

plt.xlim(-2, 2) # x軸の表示範囲
plt.ylim(-2, 2) # y軸の表示範囲
plt.xlabel('x')
plt.ylabel('y')
plt.title('An example of perceptron')
plt.savefig("perceptron.png")
