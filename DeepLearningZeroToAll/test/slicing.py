# 리스트에 대한 슬라이스 연습
nums = [0,1,2,3,4]
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:2])
print(nums[:])
print(nums[:-1])
nums[2:4] = [8, 9]
print(nums)

# numpy의 array 연습
import numpy as np

# 1차원 배열
a = np.array([1,2,3,4,5])
print(a)
print(a[1:3])
print(a[-1])
a[0:2] = 9
print(a)

# 2차원 배열
b = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]
            ])
print(b)

print(b[:, 1])      # 전체 행에서 2번째 열 출력
print(b[-1])        # 마지막 행 출력
print(b[-1, :])     # 마지막 행 출력
print(b[-1, ...])   # 마지막 행 출력
print(b[0:2, :])    # 1, 2행 출력