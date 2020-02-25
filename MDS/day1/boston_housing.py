# Boston Housing 예제
import keras
from keras.datasets import boston_housing
from keras import models, layers
import numpy as np
from keras import backend as K
import matplotlib.pyplot as plt


(train_data, train_target), (test_data, test_target) = boston_housing.load_data()

print(train_data.shape)
print(train_target.shape)
print(test_data.shape)
print(test_target.shape)

# 표준화 - 학습을 잘하기 위해 사용
mean = train_data.mean(axis=0)      # 행중심 - 13개의 값 출력
print(mean.shape)
train_data -= mean                  # 평균을 빼고
std = train_data.std(axis=0)        # 행중심 - 13개의 값 출력
print(std.shape)
train_data /= std                   # 표준편차
print(train_data[0])

test_data -= mean
test_data /= std

def build_model():
    model = models.Sequential()

    # 여러개의 층 사용, 뉴런수 설정, 활성화 함수 설정
    model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])  # 에러 절대값의 평균(낮을수록 좋다.)
    return model

# 모델 생성
model = build_model()

# 학습
model.fit(train_data, train_target, epochs=100, batch_size=1)

# 평가
test_loss, test_acc = model.evaluate(test_data, test_target)

print('\n')
print('test_acc :', test_acc, ", test_loss :", test_loss)

# kfold cross validataion
k = 4
num_val_samples = len(train_data) // k  # 101개 씩
num_epochs = 100
all_scores = []                         # 검증 점수

for i in range(k):
    print('처리중인 폴드 #', i)
    # 검증 데이터 준비: k번째 분할
    val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
    val_targets = train_target[i * num_val_samples: (i + 1) * num_val_samples]

    # 훈련 데이터 준비: 다른 분할 전체 (데이터 붙이기)
    partial_train_data = np.concatenate([train_data[:i * num_val_samples], train_data[(i + 1) * num_val_samples:]], axis=0)
    partial_train_targets = np.concatenate([train_target[:i * num_val_samples:], train_target[(i + 1) * num_val_samples:]], axis=0)

    model = build_model()       # 새로운 모델 생성

    # 학습 진행 verbose = 0 로그 출력 안함
    model.fit(partial_train_data, partial_train_targets, epochs=num_epochs, batch_size=1, verbose=0)

    # 평가 수행
    val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=0)

    # 평가 결과 추가
    all_scores.append(val_mae)

print(all_scores)
print(np.mean(all_scores))

print("*"*50, '\n')

K.clear_session()
num_epochs = 500                # 500번 수행
all_mae_histories = []          # 모든 정보 저장

for i in range(k):
    print('처리중인 폴드 #', i)
    # 검증 데이터 준비: k번째 분할
    val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
    val_targets = train_target[i * num_val_samples: (i + 1) * num_val_samples]

    # 훈련 데이터 준비: 다른 분할 전체
    partial_train_data = np.concatenate(
        [train_data[:i * num_val_samples],
         train_data[(i + 1) * num_val_samples:]],
        axis=0)
    partial_train_targets = np.concatenate(
        [train_target[:i * num_val_samples:],
         train_target[(i + 1) * num_val_samples:]],
        axis=0)

    model = build_model()
    history = model.fit(partial_train_data, partial_train_targets,
                        validation_data=(val_data, val_targets),
                        epochs=num_epochs, batch_size=1, verbose=0)
    #mae_history = history.history['val_mean_absolute_error']
    mae_history = history.history['val_mae']
    all_mae_histories.append(mae_history)

average_mae_history =  [
    np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]

# 그래프 그리기
plt.plot(range(1, len(average_mae_history) + 1), average_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()

def smooth_curve(points, factor = 0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points


model = build_model()
model.fit(train_data, train_target,
         epochs=80, batch_size=16, verbose=0)
test_mse_score, test_mae_score=model.evaluate(test_data, test_target)
print(test_mse_score, test_mae_score)