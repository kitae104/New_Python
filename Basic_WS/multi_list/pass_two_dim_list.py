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

