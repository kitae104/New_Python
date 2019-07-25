# 랜덤값으로 리스트 초기화 하기
import random

# 임의의 배열 만들기
def makeMatrix(numOfRows, numOfCols):
    matrix = []  # 빈 리스트 생성

    for row in range(numOfRows):
        matrix.append([])   # 빈 행을 추가한다.
        for col in range(numOfCols):
            matrix[row].append(random.randint(0, 99))

    return matrix

# 배열 출력하기
def printMatrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()

# 모든 원소의 합 구하기
def sumTotal(matrix):
    sum = 0
    for row in matrix:
        for value in row:
           sum += value

    return sum

# 각 열의 원소의 합계 출력
def sumRow(matrix):
    i = 0;
    for row in matrix:
        sum = 0
        for value in row:
            sum += value
        print(i, '번째 열의 합계 = ', sum)
        i += 1

# 합계가 가장 큰 행 찾기
def findMaxRow(matrix):
    maxRow = sum(matrix[0])
    indexOfMax = 0

    for row in range(1, len(matrix)):
        if sum(matrix[row]) > maxRow:
            maxRow = sum(matrix[row])
            indexOfMax = row

    print("MAX :", indexOfMax, "번째 행의 합계 : ", maxRow)

def main():
    numOfRows = 3 # eval(input('행 갯수 : '))
    numOfCols = 3 # eval(input('열 갯수 : '))

    # 주어진 행, 열 크기의 배열 만들기
    mat = makeMatrix(numOfRows, numOfCols)

    # 배열 출력
    printMatrix(mat)

    total = sumTotal(mat)
    print("전체 합계 : ", total)

    sumRow(mat)

    findMaxRow(mat)

    mat.sort()          # 첫번째 원소를 기준으로 행을 정렬한다.
    printMatrix(mat)

main()