import Basic_WS.list.RandomCharacter as RC

# 문자 리스트를 생성한다.
def createList():
    chars = []      # 빈리스트 생성

    # 소문자를 생성하고 리스트에 추가한다.
    for i in range(100):
        chars.append(RC.getRandomLowerCaseLetter())

    return chars

# 문자 리스트를 출력한다.
def displayList(chars):
    for i in range(len(chars)):
        if(i + 1) % 20 == 0:
            print(chars[i])
        else:
            print(chars[i], end=' ')

# 각 문자의 빈도수를 센다
def cntLetters(chars):
    # 0으로 초기화된 26개의 정수 리스트를 생성한다.
    counts = 26 * [0]

    # 각 리스트의 소문자를 센다
    for i in range(len(chars)):
        counts[ord(chars[i]) - ord('a')] += 1

    return counts

# 각 문자의 빈도수를 출력한다
def displayCounts(counts):
    for i in range(len(counts)):
        if(i+1) % 10 == 0:
            print(counts[i], chr(i + ord('a')))
        else:
            print(counts[i], chr(i + ord('a')), end=' ')

def main():
    list = createList()
    displayList(list)
    print()
    counts = cntLetters(list)
    displayCounts(counts)

main()