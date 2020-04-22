# 1. 라이브러리 임포트 및 버전 확인하기
import PublicDataReader as pdr
print(pdr.__version__)

# 2. 공공 데이터 포털 Open API 서비스 인증키 입력하기
serviceKey = "key"

# 3. 사용할 서비스의 인스턴스 생성하기
AptTrade = pdr.AptTradeReader(serviceKey)
AptTradeDetail = pdr.AptTradeDetailReader(serviceKey)
AptRent = pdr.AptRentReader(serviceKey)
AptOwnership = pdr.AptOwnershipReader(serviceKey)
OffiTrade = pdr.OffiTradeReader(serviceKey)
OffiRent = pdr.OffiRentReader(serviceKey)
RHTrade = pdr.RHTradeReader(serviceKey)
RHRent = pdr.RHRentReader(serviceKey)
DHTrade = pdr.DHTradeReader(serviceKey)
DHRent = pdr.DHRentReader(serviceKey)
LandTrade = pdr.LandTradeReader(serviceKey)
BizTrade = pdr.BizTradeReader(serviceKey)

# 4. 지역코드 검색하기
df_code = AptTrade.CodeFinder("백현동")                            # 지역코드 : 41135
df_code.head()

# 5. 지역, 월 별 데이터 프레임 만들기
# Function("지역코드 5자리", "계약월(YYYYMM)")
# 2020년 03월 백현동에 해당하는 자료를 Pandas DataFrame 으로 생성

df_AptTrade = AptTrade.DataReader("41135", "202003")             # 아파트매매 실거래자료 조회
df_AptTradeDetail = AptTradeDetail.DataReader("41135", "202003") # 아파트매매 실거래 상세 자료 조회

df_AptRent = AptRent.DataReader("41135", "202003")               # 아파트 전월세 자료 조회
df_AptOwnership = AptOwnership.DataReader("41135", "202003")     # 아파트 분양권전매 신고 자료 조회

df_OffiTrade = OffiTrade.DataReader("41135", "202003")           # 오피스텔 매매 신고 조회
df_OffiRent = OffiRent.DataReader("41135", "202003")             # 오피스텔 전월세 신고 조회

df_RHTrade = RHTrade.DataReader("41135", "202003")               # 연립다세대 매매 실거래자료 조회
df_RHRent = RHRent.DataReader("41135", "202003")                 # 연립다세대 전월세 실거래자료 조회

df_DHTrade = DHTrade.DataReader("41135", "202003")               # 단독/다가구 매매 실거래 조회
df_DHRent = DHRent.DataReader("41135", "202003")                 # 단독/다가구 전월세 자료 조회

df_LandTrade = LandTrade.DataReader("41135", "202003")           # 토지 매매 신고 조회
df_BizTrade = BizTrade.DataReader("41135", "202003")             # 상업업무용 부동산 매매 신고 자료 조회


# 6. 지역, 기간 별 데이터 프레임 만들기
# Function("지역코드 5자리", "시작 년월(YYYY-MM)", "종료 년월(YYYY-MM)")
df_AptTradeSum = AptTrade.DataCollector("41135", "2020-01", "2020-03")   # 기타 서비스 함수 동일