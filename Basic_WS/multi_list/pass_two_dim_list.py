# 2차원 리스트 함수에 전달하기
# 2차원 리스트 반환
def getMatrix():
    matrix = []     # 빈 리스트

    rows = 2  # eval(input("행의 갯수 : "))
    cols = 2  # eval(input("열의 갯수 : "))

    for row in range(rows):
        matrix.append([])
        for col in range(cols):
            value = eval(input("값을 입력하고 엔터를 누르세요: "))
            matrix[row].append(value)

    return matrix

# 행렬안의 모든 원소의 합을 반환
def accumulate(m):
    total = 0
    for row in m:
        total += sum(row)       # 한줄씩 합을 구함

    return total

def f(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] += 1

def printM(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()

def main():
    m = getMatrix()
    print(m)

    #원소의 합계를 출력한다.
    print('\n모든 원소의 총합은 : ', accumulate(m))

    m = [[0, 0], [0, 1]]
    printM(m)
    f(m)
    printM(m)

main()