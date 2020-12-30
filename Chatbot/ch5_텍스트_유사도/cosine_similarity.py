# 코사인 유사도 게산
from konlpy.tag import Komoran
import numpy as np
from numpy.linalg import norm

# 코사인 유사도 계산
def cos_sim(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# TDM 만들기
def make_term_doc_mat(sentence_bow, word_dics):
    freq_mat = {}

    for word in word_dics:
        freq_mat[word] = 0

    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] += 1

    return freq_mat

# 단어 벡터 만들기
def make_vector(tdm):
    vec = []
    for key in tdm:
        vec.append(tdm[key])
    return vec

# 문장 정의
sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학하였다'
sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학하였다'
sentence3 = '나는 맛잇는 밥을 뉴턴 선생님과 함께 먹었습니다.'

# 헝태소분석기를 이용해 단어 묶음 리스트 생성
komoran = Komoran()
bow1 = komoran.nouns(sentence1)
bow2 = komoran.nouns(sentence2)
bow3 = komoran.nouns(sentence3)

# 단어 묶음 리스트를 하나로 합침
bow = bow1 + bow2 + bow3
print(bow)
# ['6월', '뉴턴', '선생님', '제안', '트리니티', '입학', '6월', '뉴턴', '선생님', '제안', '대학교', '입학', '맛', '밥', '뉴턴', '선생', '님과 함께']

# 단어 묶음에서 중복제거해 단어 사전 구축
word_dics = []
for token in bow:
    if token not in word_dics:
        word_dics.append(token)

print(word_dics)
# ['6월', '뉴턴', '선생님', '제안', '트리니티', '입학', '대학교', '맛', '밥', '선생', '님과 함께']

# 문장 별 단어 문서 행렬 계산
freq_list1 = make_term_doc_mat(bow1, word_dics)
freq_list2 = make_term_doc_mat(bow2, word_dics)
freq_list3 = make_term_doc_mat(bow3, word_dics)
print(freq_list1)
# {'6월': 1, '뉴턴': 1, '선생님': 1, '제안': 1, '트리니티': 1, '입학': 1, '대학교': 0, '맛': 0, '밥': 0, '선생': 0, '님과 함께': 0}
print(freq_list2)
print(freq_list3)

# 코사인 유사도 계산
test = make_vector(freq_list1)
print(test)
# [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
doc1 = np.array(make_vector(freq_list1))
print(doc1)
# [1 1 1 1 1 1 0 0 0 0 0]

doc2 = np.array(make_vector(freq_list2))
doc3 = np.array(make_vector(freq_list3))
r1 = cos_sim(doc1, doc2)
r2 = cos_sim(doc3, doc1)
print(r1)
# 0.8333333333333335
print(r2)
# 0.18257418583505536