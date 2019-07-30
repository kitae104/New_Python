def main():
    # 문제에 대한 학생의 답안
    answers = [
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

    # 문제의 정답
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

    # 모든 답안을 평가한다.
    for i in range(len(answers)):

        correctCnt = 0
        for j in range (len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCnt += 1

        print(i, "번 학생의 정답 갯수 : ", correctCnt)

main()