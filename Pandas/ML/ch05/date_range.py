# date_range() 와 period_range() 사용
import pandas as pd
# date_range() 함수를 사용하면 여러 개의 날짜가 들어있는 배열 형태의 시계열 데이터를 만들 수 있다.
ts_ms = pd.date_range(start="2020-01-01",   # 날짜 범위의 시작
                      end=None,             # 날짜 범위의 끝
                      periods=5,            # 생성할 Timestamp의 개수
                      freq='MS',            # 시간 간격 (MS: 월의 시작일)
                      tz='ASIA/Seoul')      # 시간대(timezone)
print(ts_ms)

ts_me = pd.date_range(start="2020-01-01",   # 날짜 범위의 시작
                      end=None,             # 날짜 범위의 끝
                      periods=6,            # 생성할 Timestamp의 개수
                      freq='M',             # 시간 간격 (M: 월의 마지막일)
                      tz='ASIA/Seoul')      # 시간대(timezone)
print(ts_me)

ts_3m = pd.date_range(start="2020-01-01",   # 날짜 범위의 시작
                      end=None,             # 날짜 범위의 끝
                      periods=6,            # 생성할 Timestamp의 개수
                      freq='3M',            # 시간 간격 (3M : 3개월)
                      tz='ASIA/Seoul')      # 시간대(timezone)
print(ts_3m)

# period_range() 함수는 여려 개의 기간이 들어 있는 시계열 데이터를 만든다.
# 월 처리
pr_m = pd.period_range(start='2020-01-01',
                       end=None,
                       periods=3,       # 3개월
                       freq='M')
print(pr_m)

# 일 처리
pr_d = pd.period_range(start='2020-01-01',
                       end=None,
                       periods=40,      # 40일
                       freq='D')
print(pr_d)

# 시간 처리
pr_h = pd.period_range(start='2020-01-01',
                       end=None,
                       periods=3,       # 3시간
                       freq='2H')       # 2시간 간격
print(pr_h)