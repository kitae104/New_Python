import Basic_WS.multi_list.nearest_points as n_points

def main():
    numberOfPoints = 8  # eval(input("점의 갯수를 입력하세요 : "))

    # 점을 저장하기 위한 리스트
    points = []
    print(numberOfPoints,"개 점의 위치를 입력하세요.", end='')

    for i in range(numberOfPoints):
        point = 2 * [0]
        point[0], point[1] = eval(input("콤마로 분리하여 점의 좌표값을 입력하세요:"))
        points.append(point)

    print(points)

    p1, p2 = n_points.nearestPoints(points)

    print("(", str(points[p1][0]),",", str(points[p1][1]),")", "(", str(points[p2][0]),",", str(points[p2][1]),")")

main()
