import numpy as np

W1 = np.array([[1.5, -1, -1], [-0.5, 1, 1]]) # 1層目の重み
W2 = np.array([-1.5, 1, 1]) # 2層目の重み

# ステップ関数（入力は1行のArray型）
def step(x):
    for i in range(len(x)):
        if x[i] <= 0:
            x[i] = 0
        else:
            x[i] = 1
    return x

# xorゲート（入力は1行のArray型）
def xor(x):
    x = np.hstack((np.array([1]), x)) # 定数項のために「1」のユニットを加える
    S = step(np.dot(W1, x)) # 1層目
    S = np.hstack((np.array([1]), S)) # 定数項のために「1」のユニットを加える
    
    Y = step(np.array([np.dot(W2, S)])) # 2層目
    return Y

# サンプル
X = np.array([1, 1])
answer = xor(X)
print(answer)