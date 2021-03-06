# 합성곱 계층 클래스
import numpy as np
from DeepLearningFromScratch.common.util import im2col, col2im

class Convolution:

    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        FN, C, FH, FW = x.W.shape   # 필터
        N, C, H, W = x.shape        # 데이터

        out_h = int(1 + (H + 2*self.pad - FH) / self.stride)
        out_w = int(1 + (W + 2*self.pad - FW) / self.stride)


        # x : 4차원 배열 형태의 입력 데이터(이미지 수, 채널 수, 높이, 너비)
        # FH : 필터의 높이
        # FW : 필터의 너비
        # stride : 스트라이드
        # pad : 패딩
        col = im2col(x, FH, FW, self.stride, self.pad)  # 평탄화
        col_W = self.W.reshape(FN, -1).T                # 필터 전개, -1 기능.
        out = np.dot(col, col_W) + self.b               # 입력데이터 X 필터 + 편향

        # 축 순서 변경(N, H, W, C) --> (N, C, H, W)
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        return out

    def backword(self, dout):
        FN, C, FH, FW = self.W.reshape
        dout = dout.transpose(0, 2, 3, 1).reshape(-1, FN)

        self.db = np.sum(dout, axis=0)
        self.dW = np.dot(self.col.T, dout)
        self.dW = self.dW.transpose(1, 0).reshape(FN, C, FH, FW)

        dcol = np.dot(dout, self.col_W.T)

        # (im2col과 반대) 2차원 배열을 입력받아 다수의 이미지 묶음으로 변환한다.
        # dcol : 2차원 배열(입력 데이터)
        # input_shape : 원래 이미지 데이터의 형상（예：(10, 1, 28, 28)）
        # FH : 필터의 높이
        # FW : 필터의 너비
        # stride : 스트라이드
        # pad : 패딩
        dx = col2im(dcol, self.x.shape, FH, FW, self.stride. self.pad)

        return dx


class Pooling:
    def __init__(self, pool_h, pool_w, stride=1, pad=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        N, C, H, W = x.shape
        out_h = int(1 + (H - self.pool_h) / self.stride)
        out_w = int(1 + (W - self.pool_w) / self.stride)

        # 전개(1) : 입력 데이터를 전개 - (n행, 행*열) 갯수
        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col = col.reshape(-1, self.pool_h * self.pool_w)

        # 최댓값(2)
        out = np.max(col, axis = 1)     # 행별 최댓값(0은 열, 1은 행)

        # 적절한 모양으로 변현(3)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        return out

    def backward(self, dout):
        dout = dout.transpose(0, 2, 3, 1)

        pool_size = self.pool_h * self.pool_w
        dmax = np.zeros((dout.size, pool_size))
        dmax[np.arange(self.arg_max.size), self.arg_max.flatten()] = dout.flatten()
        dmax = dmax.reshape(dout.shape + (pool_size,))

        dcol = dmax.reshape(dmax.shape[0] * dmax.shape[1] * dmax.shape[2], -1)
        dx = col2im(dcol, self.x.shape, self.pool_h, self.pool_w, self.stride, self.pad)

        return dx