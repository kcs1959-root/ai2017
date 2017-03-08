import matplotlib.pyplot as plt
import numpy as np

# データの読み込み
data = np.load('height_weight.npy')

# データ点をプロットする
plt.plot(data[0], data[1], 'o')

# データの個数をNとする
N = np.shape(data)[1]

# 式2.1と式2.2に含まれる記号を事前に計算します
Sxn = sum([xn for xn in data[0]]) # Σ(xn)
Stn = # 書き込んでください # Σ(tn)
Sxn2 = # 書き込んでください # Σ(xn^2)
Sxntn = sum([xn * tn for xn, tn in zip(data[0], data[1])]) # Σ(xn tn)

# 式2.1と式2.2を計算します
w1 = # 書き込んでください
w0 = # 書き込んでください

# 求めた直線を描写します
t = np.arange(700, 1500, 10)
s = w1 * t + w0
plt.plot(t, s)

plt.xlabel('heights')
plt.ylabel('weights')
plt.title('Heights and weights')
plt.savefig('linear_regression.png')
