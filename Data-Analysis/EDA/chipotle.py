import pandas as pd

file_path = '../data/chipotle.tsv'
chipo = pd.read_csv(file_path, sep='\t')

item_count = chipo['item_name'].value_counts()

for idx, (val, cnt) in enumerate(item_count.iteritems()):
    print("Top", idx, ":", val, cnt)

order_count = chipo.groupby('item_name')['order_id'].count()
print(order_count[0:2])

item_quantity = chipo.groupby('item_name')['quantity'].sum()  # 주문 총량
print(item_quantity[:10])

