import Basic_WS.multi_list.nearest_points as n_points

def main():
    numberOfPoints = 8  # eval(input("점의 갯수를 입력하세요 : "))

    # 점을 저장하기 위한 리스트
    points = [[-1, 3], [-1, -1], [1, 1], [2, 0.5], [2, -1], [3,3], [4,2], [4, 0.5]]

    p1, p2 = n_points.nearestPoints(points)

    print("(", str(points[p1][0]),",", str(points[p1][1]),")", "(", str(points[p2][0]),",", str(points[p2][1]),")")

main()


