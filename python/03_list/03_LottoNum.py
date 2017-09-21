###################################################
# subject     : Lotto6
# date        : 2017-09-21 00:40
# description : Lotto6の６つの数を選択する
# Ver0.1
###################################################
import random

#変数宣言
endFlg = 0
numList = list()
sN = 0
cnt = 0

#自動選択が終わったらループ終了する
while endFlg == 0:
    #１番目のループの場合、リストにレンダム数を保存する
    if cnt == 0:
        numList.append(random.randint(1,45))
        cnt = cnt + 1

    #レンダム数を取得
    sN = random.randint(1,45)

    #取得した数が重複するかチェック
    for tempN in numList:
        if sN != tempN:
            numList.append(random.randint(1,45))
            cnt = cnt + 1
        break

    #６つの数をリストに保存した場合処理終了フラグをオンにする
    if cnt == 6:
        endFlg = 1

#リストをソートする
numList.sort()

#自動に選択した数を出力する
print("Lotto6 Auto選択結果")
print("ーーーーーーーーーーーーーーーーーーーー")
print(numList)
print("ーーーーーーーーーーーーーーーーーーーー")
print("GoodLuck")