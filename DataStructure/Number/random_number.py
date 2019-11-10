#난수 생성
import random

def test_random():
    values = [1,2,3,4]
    print(random.choice(values))
    print(random.sample(values, 2))     # 2개 추출하기
    random.shuffle(values)              # 임의로 섞기
    print(values)
    print(random.randint(0, 10))        # 0~10사이의 임의의 정수

if __name__ == "__main__":
    test_random()

# 2
# [4, 1]
# [3, 1, 2, 4]
# 6