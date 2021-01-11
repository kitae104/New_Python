# 챗봇 엔진 NER 모델 모듈
# 필요한 라이브러리 불러오기
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing

# 개체명 인식 모델 모듈
class NerModel:
    # 생성자
    def __init__(self, model_name, proprocess):

        # BIO 태그 클래스 별 레이블
        # B_FOOD : 음식
        # B_DT, BTI : 날짜, 시간
        # B_PS : 사람
        # B_OG : 조직, 회사
        # B_LC : 지역
        self.index_to_ner = {1: '0', 2:'B_DT', 3:'B_FOOD', 4:'I', 5:'B_OG',
                             6:'B_PS', 7:'B_LC', 8:'NNP', 9:'B_TI', 0:'PAD'}

        # 의도 분류 모델 불러오기
        self.model = load_model(model_name)

        # 챗봇 Preprocess 객체
        self.p = proprocess

    # 개체명 클래스 예측
    def predict(self, query):
        # 형태소 분석
        pos = self.p.pos(query)

        # 문장내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 패딩 처리
        max_len = 40
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, padding='post', value=0, maxlen=max_len)

        # 키워드별 개체명 예측
        predict = self.model.predict(np.array([padded_seqs[0]]))
        predict_class = tf.math.argmax(predict, axis=-1)

        tags = [self.index_to_ner[i] for i in predict_class.numpy()[0]]
        return list(zip(keywords, tags))

    # 개체명 태그 예측
    def predict_tags(self, query):
        # 형태소 분석
        pos = self.p.pos(query)

        # 문장내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 패딩 처리
        max_len = 40
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, padding='post', value=0, maxlen=max_len)

        # 키워드별 개체명 예측
        predict = self.model.predict(np.array([padded_seqs[0]]))
        predict_class = tf.math.argmax(predict, axis=-1)

        tags = []
        for tag_idx in predict_class.numpy()[0]:
            if tag_idx == 1 :
                continue
            tags.append(self.index_to_ner[tag_idx])

        if len(tags) == 0:
            return None

        return tags


