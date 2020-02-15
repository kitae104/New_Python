# 기울기 계산
import numpy as np
import matplotlib.pyplot as plt

def function_2(x):
    #return np.sum(x**2)     # return x[0]**2 + x[1]**2 같은 의미
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)

def numerical_gradient_no_batch(f, x):
    h = 1e-4
    grad = np.zeros_like(x) # x와 형상이 같은 배열을 생성

    for idx in range(x.size):
        tmp_val = x[idx]    # x의 idx번째 데이터 값 추출

        #f(x+h) 계산
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val    # 값 복원
    return grad

def numerical_gradient(f, X):
    if X.ndim == 1:
        return numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)

        for idx, x in enumerate(X):
            grad[idx] = numerical_gradient_no_batch(f, x)

        return grad

if __name__ == "__main__":
    res = numerical_gradient(function_2, np.array([3.0, 4.0]))
    print(res)
    res = numerical_gradient(function_2, np.array([0.0, 2.0]))
    print(res)
    res = numerical_gradient(function_2, np.array([3.0, 0.0]))
    print(res)

    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    X, Y = np.meshgrid(x0, x1)
    X = X.flatten()  # 2차원 데이터를 1차원으로 평탄화
    Y = Y.flatten()
    grad = numerical_gradient(function_2, np.array([X, Y]))     # 기울기

    plt.figure()    # 그림 크기 정하기
    plt.quiver(X, Y, -grad[0], -grad[1], angles='xy', color="#666666")  # 그래프 그리기

    plt.xlim([-2, 2])
    plt.ylim([-2, 2])

    plt.xlabel('x0')
    plt.ylabel('x1')

    plt.grid()
    # plt.legend()

    plt.draw()
    plt.show()




