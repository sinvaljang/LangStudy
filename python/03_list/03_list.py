###################################################
# subject     : リスト
# date        : 2017-09-20 11:40
###################################################

#make list
name = ["jang", "fuzimoto", "sekino"]
age = [30,23,31]

peopleInfo = [name, age]

#print list
print(name)
print(age)
print(peopleInfo)

#list indexing
print(name[0])
print(age[0])
print(peopleInfo[0])
print(peopleInfo[0][0])
print(age[0] + age[1] + age[2])

#-1は最後から取得
print(peopleInfo[-1][-1])


#make empty list
emptyList = list()
print(emptyList)

#リストのスライシング
#リスト宣言
sL = [1,2,3,4,5,6,7,8,9,10]
#0から２番目までの
print(sL[0:2])
#最初に何も指定しなかったら、一番最初になる
print(sL[:5])
print(sL[5:])

#リストの演算子
a = [1,2,3,4,5]
b = [6,7,8,9,10]

print(a + b)

print(a * 3)

#リストの内容編集
a[0] = 2
print(a)

del a[1]
print(a)

a.append(99)
print(a)