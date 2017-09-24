###################################################
# subject     : 自動販売機
# date        : 2017-09-23 09:40
# description : 関数を使用して自動販売機システムを具現
# edit        :
# Ver0.1
###################################################

#変数宣言
input_money = 0
first = True

#リストにdictionaryの飲み物を入れる
kind_coffee = {'name' : 'coffee', 'price' : 150}
kind_walter = {'name' : 'walter', 'price' : 100}
kind_coca = {'name' : 'coca'  , 'price' : 120}

kind = [kind_coffee, kind_walter, kind_coca]
kind_size = len(kind)

#関数１
#ユーザが入れたお金で飲み物を買うことができるかチェック
def chk_canbuy(input_money, price):
    chk_num = price - input_money

    if chk_num < 0:
        return True
    else:
        return False
#関数２
#お釣りを計算する
def return_money(kind, input_money, price):
    if kind == 0:
        return price - input_money
    elif kind == 1:
        return input_money - price

#ユーザに見せる飲み物の情報を作成
comment = ''
for i in range(kind_size):
    comment = comment + str(i) + ' : ' + kind[i].get('name') + '(' + str(kind[i].get('price')) + ') '

#ロジック開始
while True:
    print('----------------------------------')
    print('販売している飲み物項目。')
    print('----------------------------------')
    print(comment)
    print('----------------------------------')

    #最初のループの場合、お金を入力する
    if first :
        input_money = int(input('お金を入れてください。: \n'))
        first = False

    print('入力したお金は%d円です。\n' %input_money)

    #入力したお金が０円の場合
    if input_money == 0:
        print('お金を入れてください。')
        break

    #ユーザから飲み物を選択してもらう
    select = int(input('何を飲みたいですか。 : \n'))

    #項目以外の場合、処理を終了する
    if select < 0 or select > kind_size - 1:
        print('Wrong Input')
        print('お釣りは%d円です。' % input_money)
        break
    else:
        price = kind[select].get('price')
        item_kind = kind[select].get('name')

        #ユーザのお金で飲み物を買うことができるか判断
        if chk_canbuy(input_money, price) :
            input_money = return_money(0, input_money, price)
            print('%d円が足りないです' %input_money)
            break
        else:
            input_money = return_money(1, input_money, price)
            print('%sが出ました\n'%item_kind)

            #飲み物を買った後のお金が０円の場合
            if input_money <= 0:
                print('残高がないので終了します。')
                break

            next = int(input('もっと利用しますか[0:Ok, 1:No]'))

            #続いて飲み物を買うか確認
            if next == 1:
                print('お釣りは%d円です。' %input_money)
                break
            elif next < 0 or next > 1:
                print('Wrong Input')
                print('お釣りは%d円です。' % input_money)
                break








