# 챗봇 전처리 클래스 테스트
from utils.Preprocess import Preprocess

sent = "내일 오전 10시에 짬뽕 주문하고 싶어ㅋㅋ"

# 전처리 객체 생성
p = Preprocess(userdic='../utils/user_dic.tsv')

# 형태소 분석기 실행
pos = p.pos(sent)
print(pos) # [('내일', 'NNG'), ('오전', 'NNP'), ('10시', 'NNG'), ('에', 'JKB'), ('짬뽕', 'NNG'), ('주문', 'NNG'), ('하', 'XSV'), ('고', 'EC'), ('싶어ㅋㅋ', 'NA')]

# 품사 태그와 같이 키워드 출력
ret = p.get_keywords(pos, without_tag=False)
print(ret) # [('내일', 'NNG'), ('오전', 'NNP'), ('10시', 'NNG'), ('짬뽕', 'NNG'), ('주문', 'NNG'), ('싶어ㅋㅋ', 'NA')]

# 품사 태그 없이 키워드 출력
ret = p.get_keywords(pos, without_tag=True)
print(ret) # ['내일', '오전', '10시', '짬뽕', '주문', '싶어ㅋㅋ']