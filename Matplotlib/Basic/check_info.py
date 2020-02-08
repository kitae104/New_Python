import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

print ('버전: ', mpl.__version__)
print ('설치 위치: ', mpl.__file__)
print ('설정 위치: ', mpl.get_configdir())
print ('캐시 위치: ', mpl.get_cachedir())

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# ttf 폰트 전체개수
print(len(font_list))

# ttf 폰트 10개 출력
print(font_list[:10])

# 스타일 리스트 출력
print(plt.style.available)

# 컬러 정보를 담을 빈 딕셔너리 생성
colors = {}

# 컬러 이름과 헥사코드 확인하여 딕셔서리에 입력
for name, hex in mpl.colors.cnames.items():
    colors[name] = hex

#print(colors)
for key, value in colors.items():
    print(key, ":", value)
