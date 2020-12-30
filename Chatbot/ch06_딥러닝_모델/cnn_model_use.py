# 문장 감정 분류 CNN 모델 사용
import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing

# 데이터 읽어오기
train_file = "./chatbot_data.csv"
data = pd.read_csv(train_file, delimiter=',')
features = data['Q'].tolist()
labels = data['label'].tolist()

# 단어 인덱스 시퀀스 벡터
corpus = [preprocessing.text.text_to_word_sequence(text) for text in features]
print(corpus[0])    # ['12시', '땡']
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(corpus)
sequences = tokenizer.texts_to_sequences(corpus)  # 모든 단어에 번호를 붙임
print(sequences[0]) # [4646, 4647]

MAX_SEQ_LEN = 15        # 단어 시퀀스 벡터 크기
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post') # 빈부분을 0으로 채우기
print(padded_seqs[0])   # [4646 4647    0    0    0    0    0    0    0    0    0    0    0    0    0]

# 테스트용 데이터셋 생성
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, labels))
ds = ds.shuffle(len(features))      # 11823
test_ds = ds.take(2000).batch(20)   # 테스트 데이터셋

# 감정 분류 CNN 모델 불러오기
model = load_model('cnn_model.h5')
model.summary()
model.evaluate(test_ds, verbose=2)

# 테스트용 데이터셋의 10212번째 데이터 출력
print("단어 시퀀스 : ", corpus[10212])
# 단어 시퀀스 :  ['썸', '타는', '여자가', '남사친', '만나러', '간다는데', '뭐라', '해']
print("단어 인덱스 시퀀스 : ", padded_seqs[10212])
# 단어 인덱스 시퀀스 :  [   13    61   127  4320  1333 12162   856    31     0     0     0     0     0     0     0]
print("문장 분류(정답) : ", labels[10212])
# 문장 분류(정답) :  2

picks = [10212]
predict = model.predict(padded_seqs[picks])
predict_class = tf.math.argmax(predict, axis=1) # 분류 클래스 중에 예측 점수가 가장 큰 클래스 번호 추출
print("감정 예측 점수 : ", predict)
# 감정 예측 점수 :  [[3.6552697e-07 1.3234816e-06 9.9999833e-01]]
print("감정 예측 클래스 : ", predict_class.numpy())
# 감정 예측 클래스 :  [2]
