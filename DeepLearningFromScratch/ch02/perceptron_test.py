import DeepLearningFromScratch.ch02.perceptron_lib as lib
import numpy as np



if __name__ == "__main__":
    # AND 연산
    print(lib.AND(0, 0))
    print(lib.AND(1, 1))

    # 퍼센트론
    x = np.array([0, 1])  # 입력
    w = np.array([0.5, 0.5])  # 가중치
    b = -0.7
    res = lib.percept(x, w, b);
    print(res)

    # XOR 테스트
    print(lib.XOR(0, 0))
    print(lib.XOR(0, 1))
    print(lib.XOR(1, 0))
    print(lib.XOR(1, 1))
