###################################################
# subject     : FileReadWrite
# date        : 2017-09-26 00:20
###################################################

#空白ファイルを生成
file = open('./new.txt', 'w')
file.close()

#ファイルに文字書く
file = open('./new.txt', 'w')
for i in range(1,11):
    line_str = '%d Line\n' %i
    file.write(line_str)
file.close()

#ファイル読み込み ① radline
file = open('new.txt', 'r')
while True:
    line = file.readline()
    if not line: break
    print(line)
file.close()

#ファイル読み込み ② readlines
file = open('./new.txt', 'r')
data = file.readlines()
for line in data:
    print(line)
file.close()

#ファイル読み込み ③　read
file = open('./new.txt', 'r')
data = file.read()
print(data)
file.close()

#ファイルに続いて書く
file = open('./new.txt', 'a')
for i in range(11,21):
    line_str = '%d Line\n' %i
    file.write(line_str)
file.close()

#withを使えば、クロスがなくてもOK
with open('./new.txt', 'a') as file:
    file.write('I can do it')
