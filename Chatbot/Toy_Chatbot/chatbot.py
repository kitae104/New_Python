# 챗봇 메인
import threading
import json

from config.DatabaseConfig import *
from utils.Database import Database
from utils.BotServer import BotServer
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel
from models.ner.NerModel import NerModel
from utils.FindAnswer import FindAnswer

# 전처리 객체 생성
p = Preprocess(word2index_dic='train_tools/dict/chatbot_dict.bin', userdic='utils/user_dic.tsv')

# 의도 파악 모델
intent = IntentModel(model_name='models/intent/intent_model.h5', proprocess=p)

# 개체명 인식 모델
ner = NerModel(model_name='models/ner/ner_model.h5', proprocess=p)

# 클라이언트의 서버 연결이 수락되면 실행되는 스레드 함수
def to_client(conn, addr, params):
    db = params['db']

    try:
        db.connect()    # 디비 연결

        # 데이터 수신
        read = conn.recv(2048)  # 수신 데이터가 있을 때까지 블록킹
        print("==============================")
        print('Connection from %s' % str(addr))

        if read is None or not read:
            # 클라이언트 연결이 끊어지거나, 오류가 있는 경우
            print('클라이언트 연결 끊어짐')
            exit(0)     # 스레드 강제 종료

        # 수신된 데이터를 json 객체 데이터로 변환
        recv_json_data = json.loads(read.decode())
        print("데이터 수신 : " , recv_json_data)
        query = recv_json_data['Query']

        # 의도 파악
        intent_predict = intent.predict_class(query)
        intent_name = intent.labels[intent_predict]

        # 개체명 파악
        ner_predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)

        # 학습 DB에서 답변 검색
        try:
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(ner_predicts, answer_text)

        except:
            answer = "죄송해요 무슨 말인지 모르겠어요. 조금 더 공부 할게요."
            answer_image = None

        # Json 포맷으로 객체 생성
        send_json_data_str = {
            "Query": query,
            "Answer": answer,
            "AnswerImageUrl": answer_image,
            "Intent": intent_name,
            "NER": str(ner_predicts)
        }

        # 객체 형태로는 데이터 송수신 불가능 -> dumps로 문자열로 변환
        message = json.dumps(send_json_data_str)
        conn.send(message.encode())     # 응답 전송

    except Exception as ex:
        print(ex)

    finally:
        if db is not None:
            db.close()      # DB 연견 끊기
        conn.close()

if __name__ == '__main__':
    # 질문/답변 학습 디비 연결 객체 생성
    db = Database(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME)
    print('DB 접속')

    port = 5050     # 포트
    listen = 100    # 최대 클리이언트 연결 수

    # 봇 서버 동작
    bot = BotServer(port, listen)
    bot.create_sock()
    print("bot start")

    while True:
        conn, addr = bot.read_for_client()
        params = {
            'db':db
        }

        client = threading.Thread(target=to_client, args=(conn, addr, params))
        client.start()
