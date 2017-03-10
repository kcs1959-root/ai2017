import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

# データの作成
x1 = np.random.rand(1000, 1) * 2
x2 = np.random.rand(1000, 1) * 2
X_train = np.hstack((x1, x2))
Y_train = x1*x2 + x2

# モデルの作成
model = Sequential()
model.add(Dense(output_dim=3, input_dim=2))
model.add(Activation("sigmoid"))
model.add(Dense(output_dim=1))
model.add(Activation("linear"))

# 学習方法を決定
model.compile(loss='mse', optimizer='sgd')

# 学習
model.fit(X_train, Y_train, nb_epoch=2000)

# サンプルを試す
sample = np.array([[1.5, 2.0]])
answer = model.predict(sample)

print(answer)
