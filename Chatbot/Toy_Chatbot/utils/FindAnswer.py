# 챗봇 답변 검색 모듈
class FindAnswer:
    def __init__(self, db):
        self.db = db            # DB 정보

    # 검색 쿼리 생성(의도명과 개체명 이용)
    def _mak_query(self, intent_name, ner_tag):
        sql = "select * from chatbot_train_data"

        # 의도명만 있는 경우
        if intent_name != None and ner_tag == None:
            sql = sql + " where intent='{}' ".format(intent_name)
        # 의도명과 개체명이 같이 있는 경우
        elif intent_name != None and ner_tag != None:
            where = ' where intent="%s" ' % intent_name
            if(len(ner_tag) > 0):
                where += 'and ('
                for ne in ner_tag:
                    where += " ner like '%{}%' or ".format(ne)
                where = where[:-3] + ')'
            sql = sql + where

        # 동일한 답변이 2개 이상인 경우, 랜덤으로 선택
        sql = sql + " order by rand() limit 1"
        return sql

    # 답변 검색
    def search(self, intent_name, ner_tags):
        # 의도명, 개체명으로 답변 검색
        sql = self._mak_query(intent_name, ner_tags)
        answer = self.db.select_one(sql)

        # 검색되는 답변이 없으면 의도명만 검색
        if answer is None:
            sql = self._mak_query(intent_name, None)
            answer = self.db.select_one(sql)

        return (answer['answer'], answer['answer_image'])

    # NER 태그를 실제 입력된 단어로 변환
    def tag_to_word(self, ner_predicts, answer):
        for word, tag in ner_predicts:
            # 변환해야하는 태그가 있는 경우 추가
            if tag == 'B_FOOD' or tag == 'B_DT' or tag == 'B_TI':
                answer = answer.replace(tag, word)

        answer = answer.replace('{', '')
        answer = answer.replace('}', '')
        return answer