import sys
import time

from student import *
from easygui import *

math_1 = '类型算式1 x +/-/*// y'
math_2 = '类型算式2 x +/- y +/- z'
math_3 = '类型算式3 x +/- y * z'
math_4 = '类型算式4 x +/- y / z'
math_type_map = {
    math_1: math1,
    math_2: math2,
    math_3: math3,
    math_4: math4,
}
msg = "口算题卡"
m_choice = multchoicebox(
    msg,
    '选择',
    [math_1, math_2, math_3, math_4]
)
print("选择的题目类型", m_choice)
fieldNames = ["算式最小值", "算式最大值", "生成题目数量"]
fieldValues = []  # we start with blanks for the values
fieldValues = multenterbox(msg, "口算题卡", fieldNames)
minx = fieldValues[0]
maxx = fieldValues[1]
num = fieldValues[2]
if not minx:
    msgbox("最小值不能为空")
else:
    minx = int(minx)
if not maxx:
    msgbox("最大值不能为空")
elif int(maxx) > 10000:
    msgbox("最大值必须小于10000")
else:
    maxx = int(maxx)
if not num:
    msgbox("题目数量不能为空")
else:
    num = int(num)

try:
    pass
except:
    pass

# math1(minx, maxx)
# math2(minx, maxx)
# math3(minx, maxx)
# math4(minx, maxx)

data = []
for i in range(num):
    k = random.randint(0, len(m_choice) - 1)
    print('k')
    print(k)
    data_str = math_type_map[m_choice[k]](minx, maxx)
    data.append(data_str)
print('data')
print(data)

l = int(num / 4)

str_1 = '\t'.join(data[0:l])
str_2 = '\t'.join(data[l:2*l])
str_3 = '\t'.join(data[2*l:3*l])
str_4 = '\t'.join(data[3*l:4*l])
print('打印到控制台')
full_str = '\n'.join([str_1, str_2, str_3, str_4])
print('\n'.join([str_1, str_2, str_3, str_4]))
# format_rjust()
msgbox('\n'.join([str_1, str_2, str_3, str_4]))

import os
import datetime
if not os.path.exists('doc'):
    os.mkdir('doc')

import random
random.randint(1, 20)
with open("./doc/{}.doc".format(datetime.datetime.now().strftime('%Y%m%d:%H%M%S%f')), 'a') as f:
    f.write(full_str)
