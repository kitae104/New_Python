# 자연어 처리(리뷰 예측)
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from numpy import array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten, Embedding

# 텍스트 리뷰 자료를 지정합니다.
docs = ["너무 재밌네요", "최고예요", "참 잘 만든 영화예요", "추천하고 싶은 영화입니다", "한번 더 보고싶네요",
        "글쎄요", "별로예요", "생각보다 지루하네요", "연기가 어색해요", "재미없어요"]

# 긍정 리뷰는 1, 부정 리뷰는 0으로 클래스를 지정합니다.
classes = array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

# 토큰화
token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)     # 토큰화 된 결과를 출력해 확인

# 토큰에 지정된 인덱스로 새로운 배열 생성
x = token.texts_to_sequences(docs)
print(x)

# 패딩(서로 다른 길이의 데이터를 4로 맞추어 준다)
padded_x = pad_sequences(x, 4)
print(padded_x)

#딥러닝 모델
print("\n딥러닝 모델 시작:")

#임베딩에 입력될 단어의 수를 지정
word_size = len(token.word_index) + 1
print(word_size)

#단어 임베딩을 포함하여 딥러닝 모델을 만들고 결과를 출력
model = Sequential()
model.add(Embedding(word_size, 8, input_length=4))      # 패딩과정을 통해 입력 길이는 4로 설정
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.summary()

# 모델 컴파일
model.compile(loss='binary_crossentropy',      # 2개 중에 1개를 선택하는 경우
              optimizer='adam',
              metrics=['accuracy'])

model.fit(padded_x, classes, epochs=20)
print("\n Accuracy: %.4f" % (model.evaluate(padded_x, classes)[1]))
