'''
1.加参数
2.方法二改掉
3.循环输出混合算式
4.看PDF
'''
import random


def format_rjust(data):
    return str(data).rjust(17)


def math1(minn, maxx):  # 加减混合
    a = ['+', '-']
    tot = random.randint(0, 1)  # 第一个随机运算符号
    tot2 = random.randint(0, 1)  # 第二个随机运算符号
    fir = random.randint(minn, maxx)  # 第一个数
    sec = random.randint(minn, maxx)  # 第二个数
    thi = random.randint(minn, maxx)  # 第三个数
    # print('%s%s%s%s%s=(    )'%(format_rjust(fir),a[tot],format_rjust(sec),a[tot2],format_rjust(thi)),end='  ')#公式
    out = str(fir) + a[tot] + str(sec) + a[tot2] + str(thi) + '=(    )'
    print(format_rjust(out), end='  ')
    return format_rjust(out)


def math2(minn, maxx):  # a 加减乘除 b
    a = ['+', '-', '*', '/']
    tot = random.randint(0, 3)  # 第随机运算符号
    fir = random.randint(minn, maxx)  # 第一个数
    sec = random.randint(minn, maxx)  # 第二个数

    if tot == 3:
        while not sec:
            sec = random.randint(minn, maxx)
        if fir % sec != 0:
            fir *= sec
    # print('%s%s%s=(    )'%(format_rjust(fir),a[tot],format_rjust(sec)),end='  ')#公式
    out = str(fir) + a[tot] + str(sec) + '=(    )'
    print(format_rjust(out), end='  ')
    return format_rjust(out)


def math3(minn, maxx):  # （a +/- b）*c
    a = ['+', '-']
    tot = random.randint(0, 1)  # 随机运算符号
    fir = random.randint(minn, maxx)  # 第一个数
    sec = random.randint(minn, maxx)  # 第二个数
    thi = random.randint(minn, maxx)  # 第三个数
    # print('(%s%s%s)*%s=(    )'%(format_rjust(fir),a[tot],format_rjust(sec),format_rjust(thi)),end='  ')
    out = '(' + str(fir) + a[tot] + str(sec) + ')*' + str(thi) + '=(    )'
    print(format_rjust(out), end='  ')
    return format_rjust(out)


def math4(minn,maxx):#(a +/- b)/c
    a=['+','-']
    tot=random.randint(0,1)#随机运算符号
    num1=random.randint(minn,maxx)#被除数（a +/- b的值）
    num2=random.randint(minn,maxx)#除数（c的值）
    result=num1*num2#被除数和除数的积
    if a[tot]=='+':#符号为"+"
        fir=random.randint(0,num1)#a的值
        sec=result-fir#b的值
        #保证此时a和b的和等于前面算好的的值
    else:#符号为"-"
        fir=random.randint(result, result+100)
        sec=fir-result
        #保证此时a和b的差等于前面算好的被除数的值，即保证算式能够除尽
    #print('(%s%s%s)/%s=(    )'%(format_rjust(fir),a[tot],format_rjust(sec),format_rjust(num2)),end='  ')
    out='('+str(fir)+a[tot]+str(sec)+')/'+str(num2)+'=(    )'
    print(format_rjust(out),end='  ')
    return format_rjust(out)

# for i in range(10):
#     for j in range(4):
#         k=random.randint(1, 4)
#         if k==1:
#             math1(1, 10)
#         if k==2:
#             math2(1, 10)
#         if k==3:
#             math3(1, 10)
#         if k==4:
#             math4(1, 10)
#     print('\n')