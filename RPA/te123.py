import pandas as pd

data = pd.read_excel(r'C:\Users\PC\Desktop\Capstion\image\짧은시_Ocr_Kor_Filter_Content_Morphs.xlsx')
data = data.values.tolist()
test = []
for i in data :
    for ii in i :
        test1 = (str(ii).replace(",",""))
        test2 = test1.replace("(","").replace(")","")
        test3 = test2.replace("'","")
        test4 = test3.replace(" ",",")
        test5 = test4.split(",")
        test.append(test5)
print(test)

        
        
         



