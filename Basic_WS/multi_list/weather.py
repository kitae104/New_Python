# 10일 동안의 일간 평균 온도와 습도를 계산하기
def main():
    NUMBER_OF_DAYS = 10
    NUMBER_OF_HOURS = 24

    # 데이터를 초기화하기
    data = []

    for i in range(NUMBER_OF_DAYS):
        data.append([])
        for j in range(NUMBER_OF_HOURS):
            data[i].append([])
            data[i][j].append(0)    # 온도
            data[i][j].append(0)    # 습도

    f = open("../Datas/weather.txt", 'r')
    # 입력 재지정을 사용하여 파일로부터 입력을 받아들인다.
    for k in range(NUMBER_OF_DAYS * NUMBER_OF_HOURS):
        fline = f.readline()
        print(fline)
        line = fline.split()
        print(line)
        day = eval(line[0])
        hour = eval(line[1])
        temperature = eval(line[2])
        humidity = eval(line[3])
        data[day-1][hour-1][0] = temperature
        data[day-1][hour-1][1] = humidity

    # 일간 평균 온도와 습도를 계산한다.
    for i in range(NUMBER_OF_DAYS):
        dailyTemperatureTotal = 0
        dailyHumidityTotal = 0
        for j in range(NUMBER_OF_HOURS):
            dailyTemperatureTotal += data[i][j][0]
            dailyHumidityTotal += data[i][j][1]

        # 결과를 출력한다.
        print(str(i) + "일의 평균 온도는" + str(dailyTemperatureTotal / NUMBER_OF_HOURS) + "입니다.")
        print(str(i) + "일의 평균 습도는" + str(dailyHumidityTotal / NUMBER_OF_HOURS) + "입니다.")

main()