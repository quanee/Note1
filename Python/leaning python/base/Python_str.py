﻿

# 格式化表达式
# 4(可以是变量)指定精度
print('%f, %.2f, %.*f' % (1 / 3.0, 1 / 3.0, 4, 1 / 3.0))

# 字典键值
print('%(n)d %(x)s' % {'n': 1, 'x': 'abc'})

reply = '''
Greetings...
Hello %(name)s!
Your age squared is %(age)s
'''

values = {'name': 'moonboss', 'age': 40}

print(reply % values)

# vars()返回字典 包含本函数调用时存在的变量
print(vars())

# 3.x格式化方法
print('{0}, {1} and {2}'.format('moon', 'boss', 'max'))
print('{name}, {nicname}, {age}'.format(name='moonboss', nicname='MaxKim', age='23'))
print('{name}, {0}, {age}'.format('MaxKim', name='moonboss', age='23'))


import sys
# 键
print('My {1[name]} runs {0.platform}'.format(sys, {'name': 'laptop'}))
# 属性
print('My {config[name]} runs {sys.platform}'.format(sys=sys, config={'name': 'laptop'}))
# 偏移值
somelist = list('SPAM')