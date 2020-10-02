# 자연어 처리
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

# 전처리할 텍스트를 정합니다.
text = '해보지 않으면 해낼 수 없다'
result = text_to_word_sequence(text)
print(result)

docs = ['먼저 텍스트의 각 단어를 나누어 토큰화 합니다.',
       '텍스트의 단어로 토큰화 해야 딥러닝에서 인식됩니다.',
       '토큰화 한 결과는 딥러닝에서 사용 할 수 있습니다.',
       ]

token = Tokenizer()
token.fit_on_texts(docs)

#Tokenizer()의 word_counts 함수는 순서를 기억하는 OrderedDict클래스를 사용
print("\n단어 카운트:\n", token.word_counts)         # 각 단어의 갯수
print("\n문장 카운트: ", token.document_count)       # 문장의 갯수
print("\n각 단어가 몇개의 문장에 포함되어 있는가:\n", token.word_docs)   # 각 단어가 몇개의 문장에 있는가
print("\n각 단어에 매겨진 인덱스 값:\n",  token.word_index) # 각 단어의 인덱스

text = "오래동안 꿈꾸는 이는 그 꿈을 닮아간다"
token = Tokenizer()
token.fit_on_texts([text])
print("\n각 단어에 매겨진 인덱스 값:\n", token.word_index)

x = token.texts_to_sequences([text])
print("\n인덱스 : \n", x)

# 인덱스 수에 하나를 추가해서 원-핫 인코딩 배열 만들기
word_size = len(token.word_index) + 1
x = to_categorical(x, num_classes=word_size)
print("\n벡터화 : \n", x)