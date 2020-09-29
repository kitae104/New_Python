import pandas as pd

url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
c=pd.read_csv(url)
print(c)


df_ss = pd.read_csv('ss.csv', encoding="MS949")
df_ss.set_index('date', inplace=True)

df_lg = pd.read_csv('lg.csv', encoding="MS949")
df_lg.set_index('date', inplace=True)

df_merge = pd.DataFrame()
df_merge['삼성전자'] = df_ss['total']
df_merge['LG전자'] = df_lg['total']
print(df_merge)