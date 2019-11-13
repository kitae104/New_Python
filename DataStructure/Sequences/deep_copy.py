# 깊은 복사 이해하기
myList = [1,2,3,4]
print(myList)
# [1, 2, 3, 4]

myList.remove(2)

newList = myList[:]
print(newList)
# [1, 3, 4]

newList2 = list(myList)
print(newList2)
# [1, 3, 4]

people = {"버피", "에인절", "자일스"}
print(people)
# {'버피', '자일스', '에인절'}

slayers = people.copy()
print(slayers)
# {'버피', '자일스', '에인절'}

slayers.remove("버피")
print(slayers)
# {'자일스', '에인절'}
print(people)
# {'버피', '자일스', '에인절'}

myDict = {"안녕":"OK"}
print(myDict)
# {'안녕': 'OK'}

newDict = myDict.copy()
newDict["안녕"] = "YES"
print(myDict)
# {'안녕': 'OK'}
print(newDict)
# {'안녕': 'YES'}

# 깊은 복사 사용하기
import copy
myObj = [1,2,3,4]
newObj = myObj
print(newObj)
newObj2 = copy.deepcopy(myObj)
print(newObj2)

myObj.remove(2)
print(newObj)
print(newObj2)
