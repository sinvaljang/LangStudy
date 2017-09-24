###################################################
# subject     : Function
# date        : 2017-09-23 09:10
###################################################

#関数の宣言
def sum1(a, b):
    return a + b

print(sum1(1,2))

def sum2(a, b):
    result = a + b
    return result

print(sum2(3,4))

result2 = sum2(5,6)
print(result2)

#パラメーターの数を指定しない場合
def sum3(*args):
    sum_result = 0
    for i in args:
        sum_result = sum_result + i
    return sum_result

print(sum3(1,2,3,4,5,6,7,8,9,10))

def calc(kind, *args):
    result = 0
    if kind == 'plus':
        for i in args:
            result = result + i
    elif kind == 'minus':
        for i in args:
            result = result - i

    return result

print(calc('plus', 1,2,3,4))
print(calc('minus', 4,3,2,1))

#パラメーターの初期化
def say_whoami(name, age, men = True):
    print('私の名前は%sです' %name)
    print('私の年齢は%dです' %age)

    if men :
        print('私は男です')
    else :
        print('私は女です')

say_whoami('Anguk', 30)
say_whoami('Mai', 24, False)

#グローバル変数使用方法
a = 100

def vartest1(a):
    a = a + 1

vartest1(a)
print(a)

def vartest2():
    global a
    a = a + 1

vartest2()
print(a)

def vartest3(a):
    a = a + 1
    return a

print(vartest3(a))


