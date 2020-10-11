################################################################################
# 상태유지 LSTM 모델
# - 현재 학습된 상태가 다음 학습 시 초기 상태로 전달
################################################################################
# 데이터 관련
import numpy as np
from tensorflow.keras.utils import to_categorical

# 모델 관련
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# 콜밸 처리
from tensorflow.keras.callbacks import Callback

# 그래프 관련
import matplotlib.pyplot as plt

# 동일한 결과를 얻기 위해 시드를 고정한다.
from tensorflow.python.keras.applications.imagenet_utils import obtain_input_shape

np.random.seed(5)

########################################
# 손실 이력 클래스 정의
########################################
class LossHistory(Callback):
    def init(self):
        self.losses = []

    def on_epoch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

################################################################################
# 1 데이터 준비
################################################################################
########################################
# 코드 변환 사전
########################################
# code2idx : 코드를 숫자로 변환
code2idx = {'c4':0, 'd4':1, 'e4':2, 'f4':3, 'g4':4, 'a4':5, 'b4':6,
            'c8':7, 'd8':8, 'e8':9, 'f8':10, 'g8':11, 'a8':12, 'b8':13}
# idx2code : 숫자를 코드로 변환
idx2code = {0:'c4', 1:'d4', 2:'e4', 3:'f4', 4:'g4', 5:'a4', 6:'b4',
            7:'c8', 8:'d8', 9:'e8', 10:'f8', 11:'g8', 12:'a8', 13:'b8'}

####################################################################################################
# seq2dataset(시퀀스, 윈도우크기):
# 사전을 이용해서 순차적인 음표를 우리가 지정한 윈도우 크기만큼 잘라 데이터셋을 생성하는 함수를 정의
####################################################################################################
def seq2dataset(seq, window_size):
    dataset = []
    for i in range(len(seq)-window_size):
        subset = seq[i:(i+window_size+1)]
        dataset.append([code2idx[item] for item in subset])
    return np.array(dataset)

# 시퀀스 데이터 정의 (나비야 음계)
seq = ['g8', 'e8', 'e4', 'f8', 'd8', 'd4', 'c8', 'd8', 'e8', 'f8', 'g8', 'g8', 'g4',
       'g8', 'e8', 'e8', 'e8', 'f8', 'd8', 'd4', 'c8', 'e8', 'g8', 'g8', 'e8', 'e8', 'e4',
       'd8', 'd8', 'd8', 'd8', 'd8', 'e8', 'f4', 'e8', 'e8', 'e8', 'e8', 'e8', 'f8', 'g4',
       'g8', 'e8', 'e4', 'f8', 'd8', 'd4', 'c8', 'e8', 'g8', 'g8', 'e8', 'e8', 'e4']

################################################################################
# 2 데이터셋 준비
################################################################################
dataset = seq2dataset(seq, window_size = 4)
print(dataset.shape)
print(dataset)

x_train = dataset[:, 0:4]
y_train = dataset[:, 4]
max_idx_value = 13

########################################
# 입력 값 정규화
########################################
x_train = x_train / float(max_idx_value)
# 입력을 (샘플 수, 타입스탭, 특성 수) 형태로 변환
x_train = np.reshape(x_train, (50, 4, 1))   # LSTM에서 사용을 위한 형 변환 중요

y_train = to_categorical(y_train)           # 레벨 값에 대한 one-hot 인코딩
one_hot_vec_size = y_train.shape[1]
print("one hot encoding vector size is ", one_hot_vec_size)

################################################################################
# 3. 모델 구성하기
################################################################################
# LSTM 신경망
model = Sequential()
model.add(LSTM(128, batch_input_shape=(1, 4, 1), stateful=True))
model.add(Dense(one_hot_vec_size, activation='softmax'))
model.summary()

################################################################################
# 4. 모델 학습 과정
################################################################################
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# 손실 이력 객체 생성
history = LossHistory()
history.init()

################################################################################
# 5. 모델 학습 시키기
################################################################################
num_epochs = 2000

for epoch_idx in range(num_epochs):
    print('epochs : ' + str(epoch_idx))
    model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2, shuffle=False, callbacks=[history])
    model.reset_states()        # 모델 상태 초기화

################################################################################
# 6. 학습과정 살펴보기 모델 학습 시키기
################################################################################
plt.plot(history.losses)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()

################################################################################
# 7. 모델 평가하기
################################################################################
scores = model.evaluate(x_train, y_train, batch_size=1)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))
model.reset_states()

################################################################################
# 8. 모델 사용하기
################################################################################
pred_count = 50     # 최대 예측 개수 정의

seq_out = ['g8', 'e8', 'e4', 'f8']
pred_out = model.predict(x_train, batch_size=1)

for i in range(pred_count):
    idx = np.argmax(pred_out[i])        # one-hot 인코딩을 인덱스 값으로 변환
    seq_out.append(idx2code[idx])       # seq_out는 최종 악보이므로 인덱스 값을 코드로 변환하여 저장

model.reset_states()
print("one step song prediction : ", seq_out)

# 곡 전체 예측
seq_in = ['g8', 'e8', 'e4', 'f8']
seq_out = seq_in
seq_in = [code2idx[it] / float(max_idx_value) for it in seq_in]

for i in range(pred_count):
    sample_in = np.array(seq_in)
    sample_in = np.reshape(sample_in, (1, 4, 1))  # 샘플 수, 타입 스탭, 속성 수
    pred_out = model.predict(sample_in)
    idx = np.argmax(pred_out)
    seq_out.append(idx2code[idx])
    seq_in.append(idx / float(max_idx_value))
    seq_in.pop(0)

model.reset_states()
print("full song prediction : ", seq_out)