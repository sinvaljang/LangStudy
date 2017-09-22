###################################################
# subject     : Dictionary
# date        : 2017-09-22 11:00
###################################################

#宣言
student = {'name' : 'jang', 'age' : 30}

print(student)
print(student['name'])
print(student['age'])

#キーで値取得
student['class'] = 1
print(student['class'])

#キー削除
print(student)
del student['class']
print(student)

#dictionaryからキーをリスト形式で取得
print(student.keys())

for key in student.keys():
    print(key)

st_key_list = list(student.keys())
print(st_key_list)

#dictionaryから値をリスト形式で取得
print(student.values())
for val in student.values():
    print(val)

st_val_list = list(student.values())
print(st_val_list)

#dictionaryからキー、値をリスト形式で取得
print(student.items())
for all in student.items():
    print(all)
st_all_list = list(student.items())
print(st_all_list)

#dictionaryからキーで値を取得する
#getはキーがなかったらNoneをリターンする
print(student.get('name'))
print(student.get('class'))

if(student.get('class')):
    print('clsss ari')
else:
    print('class nasi')


#dictionaryの内容を削除
print(student)
student.clear()
print(student)

