###################################################
# subject     : 数ゲーム
# date        : 2017-09-20 11:40
# description : ランダムで生成された数をユーザが答えを合わせる
# Ver0.1
###################################################
import random

#変数初期化
ranNum = 0
userNum = 0
tryNum = 5

#レンダム数を生成
ranNum = random.randint(1,10)

print("おはよう。私はジャンと申します。私と簡単なゲームをしましょうか")
print("私がレンダムの数を生成しました。その数は１から10の間の数です。")
print("あなたに5回の機会をあげます。\n")

#入力がレンダム数と一致する場合。または、チャンスがなくなった場合まで
while userNum != ranNum and tryNum > 0:
    print("残りチャンスは%d\n" %tryNum)

    #ユーザの入力を受ける
    userNum = int(input("数を入力してください : \n"))

    #ユーザ入力数 > レンダム数
    if userNum > ranNum:
        print("Too High\n")
    #ユーザ入力数 < レンダム数
    elif userNum < ranNum:
        print("Too Low\n")

    #チャンスをマイナスする
    tryNum = tryNum - 1

print("レンダム数は %dでした" %ranNum)

#ユーザ入力数 ＝ レンダム数
if userNum == ranNum:
    print("you win")
#ユーザ入力数 != レンダム数
else:
    print("you lose")
