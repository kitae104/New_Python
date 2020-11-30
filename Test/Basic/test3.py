import numpy as np
X_data = np.array(([[0,0],[0,1],[1,0],[1,1]]))
XOR = np.array(([0,1,1,0]))

from sklearn.neural_network import MLPClassifier

XOR_model = MLPClassifier(hidden_layer_sizes=(2), activation='tanh', solver='lbfgs')
XOR_model.fit(X_data,XOR)
print(('모델평가 : ' + str(XOR_model.score(X_data, XOR))))
print(('예측 : ' + str(XOR_model.predict((np.array(([[1,1]])))))))
