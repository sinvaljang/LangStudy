###################################################
# subject     : 学生情報管理
# date        : 2017-09-21 00:40
# description : 学生の情報をdictionaryに保存し、リストに保存する
# Ver0.1
###################################################

#変数宣言部
endFLg = 0
name = ''
age = 0
score = 0
nFlg = 0
stu_list = list()

print('学生管理システムにようこそ。\n')

#ユーザから終了を入力されるまで
while endFLg == 0 :

    #学生情報を入力する
    name = input('名前を入力してください :')
    age = int(input('年齢を入力してください :'))
    score = int(input('成績を入力してください : \n'))

    #入力した情報をdictionaryに変換
    student = {'name' : name, 'age' : age, 'score' : score}

    #学生リストにdictionaryを保存する
    stu_list.append(student)
    for st in stu_list :
        print(st)

    #次の処理を入力する
    nFlg = 0
    while nFlg == 0 :
        endFLg = int(input('終了（１）　登録（０）\n'))

        #ユーザ入力範囲チェック
        if endFLg > 1 or endFLg < 0:
            print('Wrong Input')
            endFLg = 0
        #範囲以内の場合
        else:
            if endFLg == 1:
                print('終了します')
            else:
                print('次の入力をします')
            nFlg = 1
