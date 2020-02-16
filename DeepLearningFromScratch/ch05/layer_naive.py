# 곱셈 계층 구현
class MulLayer:
    def __init__(self):
        self.x = None       # 인스턴스 변수에 대한 초기화
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self, dout):
        dx = dout * self.y      # x와 y를 바꾼다.
        dy = dout * self.x

        return dx, dy

# 덧셈 계층
class AddLayer:
    def __init__(self):
        pass                    # 아무것도 하지 않음

    def forward(self, x, y):
        out = x + y
        return out

    def backward(self, dout):   # dout : 미분값
        dx = dout * 1
        dy = dout * 1
        return dx, dy


