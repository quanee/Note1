

# 位置:从左至右匹配
# func(value)
#
# 关键字参数:通过参数名匹配 (name=value)
# func(name=value)
# func(**dict)
#
# 默认参数:为没有传入值的参数定义参数值 (name=value)
#
# 可变参数:收集任意多基于位置或关键字的参数 *开头
# func(*sequence)
#
# 可变参数解包: 传递任意多基于位置或关键字的参数 *开头
#
# Keyword-only参数: 参数必须按照名称传递
#
# 位置参数, 关键字参数, *sequence形式组合, **dict

'''
参数匹配步骤:
        通过位置分配非关键字参数
        通过变量名分配关键字参数
        其他额外的非关键字参数分配到*name元组
        其他额外的关键字参数分配到**name字典中
        用默认值分配给在头部未得到分配的参数
'''

def f(a, b, c):
    print(a, b, c)


# 位置参数
f(1, 2, 3)
# 关键字参数
f(c=3, a=1, b=2)

f(1, c=3, b=2)


# 默认参数
def f(a, b=2, c=3):
    print(a, b, c)


f(1)
f(a=1)
f(1, 4)
f(1, 4, 5)
# 跳过默认参数
f(1, c=6)


# 关键字参数和默认参数混合
def func(moon, boss, mas=0, kim=0):
    print((moon, boss, mas, kim))


func(1, 2)  # (1, 2, 0, 0)
func(1, kim=1, boss=0)  # (1, 0, 0, 1)
func(moon=1, boss=2)  # (1, 2, 0, 0)
func(mas=1, boss=2, moon=3)  # (3, 2, 1, 0)
func(1, 2, 3, 4)  # (1, 2, 3, 4)


# 任意参数
# 收集参数
def f(*args):
    print(args)


f()  # ()
f(1)  # (1,)
f(1, 2, 3, 4)  # (1, 2, 3, 4)


def f(**args):
    print(args)


f()  # {}
f(a=1, b=2)  # {'a': 1, 'b': 2}


def f(a, *pargs, **kargs):
    print(a, pargs, kargs)


f(1, 2, 3, x=1, y=2)  # 1 (2, 3) {'x': 1, 'y': 2}


# 解包参数
def func(a, b, c, d):
    print(a, b, c, d)


args = (1, 2)
args += (3, 4)
func(*args)  # 1 2 3 4

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)  # 1 2 3 4

func(*(1, 2), **{'d': 4, 'c': 4})  # 1 2 4 4
func(1, *(2, 3), **{'d': 4})  # 1 2 3 4
func(1, c=3, *(2, ), **{'d': 4})  # 1 2 3 4
func(1, *(2, 3), d=4)  # 1 2 3 4
func(1, *(2, ), c=3, **{'d': 4})  # 1 2 3 4


def tracer(func, *pargs, **kargs):
    print('calling: ', func.__name__)
    return func(*pargs, **kargs)


def func(a, b, c, d):
    return a + b + c + d


print(tracer(func, 1, 2, c=3, d=4))


# keyword-only参数c(出现在*args之后 必须指定c值)
def kwonly(a, *b, c):
    print(a, b, c)


kwonly(1, 2, c=3)
kwonly(1, c=3)


def kwonly(a, *, b, c):
    print(a, b, c)


kwonly(1, b=2, c=3)


def kwonly(a, *, b='moon', c='boss'):
    print(a, b, c)


kwonly(1)
kwonly(1, b=2, c=3)


# keyword-only参数必须编写在**args任意关键字形式之前


# 交集
def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other:
                break
            else:
                res.append(x)

    return res


# 并集
def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)

    return res


s1, s2, s3 = 'SPAM', 'SCAM', 'SLAM'

print(intersect(s1, s2))
print(union(s1, s2))


# 模拟print
import sys
def print3x(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print3x("abcd")


def print3x(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs:
        raise TypeError('extar keywords: %s' % kargs)

    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

