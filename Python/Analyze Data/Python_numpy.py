import numpy as np


v = np.arange(10)
print(v)
print(v.dtype)
print(v.shape)

# 返回列表
vstep = np.arange(0, 10, 0.5)
print(vstep)
print(vstep * 10)

# 等差数列 初始值1 终止值19 元素个数为10
print(np.linspace(1, 19, 10))

# 等比数列
from math import e
print(np.logspace(1, 20, 10, endpoint=False, base=e))

# 创建全0整型向量
print(np.zeros(10, np.int))
print(np.empty(10, np.int))

# 创建随机数向量
print(np.random.randn(10))


s = 'Hello, Python!'
print(np.fromstring(s, dtype=np.int8))


def multiply99(i, j):
    return (i + 1) * (j + 1)


print(np.fromfunction(multiply99, (9, 9)))


# 数组
a = np.array([np.arange(3), np.arange(3)])
print(a)
print(a.shape)  # 形状
print(a.ndim)  # 维度

# 单位矩阵
print(np.identity(9).astype(np.int8))
print(a.tolist())
print(type(a.tolist()))

# 查看ndarray数据类型
print(set(np.typeDict.values()))

# 结构数组
goodslist = np.dtype([('name', np.str_, 50), ('location', np.str_, 30), ('price', np.float16), ('volume', np.int32)])

goods = np.array([('Gree Airconditioner', 'JD.com', 6245, 1),
                  ('Sony Blueray Player', 'Amazon,com', 3210, 2),
                  ('Apple Mackbook Pro 13', 'Tmall.com', 12388, 5),
                  ('iPhoneSE', 'JD.com', 4588, 2)], dtype=goodslist)

print(goods)

# 使用字典定义结果数组
goodsdict = np.dtype({'names': ['name', 'location', 'price', 'volume'], 'formats': ['S50', 'S30', 'f', 'i']})

goods_new = np.array([('Gree Airconditioner', 'JD.com', 6245, 1),
                      ('Sony Blueray Player', 'Amazon,com', 3210, 2),
                      ('Apple Mackbook Pro 13', 'Tmall.com', 12388, 5),
                      ('iPhoneSE', 'JD.com', 4588, 2)], dtype=goodsdict)

print(goods_new)


# 索引与切片

# ":"分割起止位置与间隔 ","表示不同维度 "..."遍历剩余维度
a = np.arange(1, 20, 2)

print(a)
print(a[3])
print(a[1:4])
print(a[:2])
print(a[-2])
print(a[::-1])

b = np.arange(24).reshape(2, 3, 4)
print(b)
print(b.shape)
print(b[1, 1, 2])
print(b[0, 2, :])
print(b[0, 2])
print(b[0, ...])
print(b[0])
print(b[:, 1])
print(b[:, :, 1])
print(b[..., 1])
print(b[0, ::2, -2])
print(goods['name'])
print(goods[3])
print(goods[3]['name'])
print(sum(goods['volume']))

# 逻辑索引(布尔索引 条件索引)
print(b[b >= 15])
print(b[~(b >= 15)])
# 逻辑运算符and, or, 在布尔数组中无效
print(b[(b >= 5) & (b <= 15)])
b_bool1 = np.array([False, True], dtype=bool)
print(b[b_bool1])
b_bool2 = np.array([False, True, True], dtype=bool)
b_bool3 = np.array([False, True, True, False], dtype=bool)
print(b[b_bool1, b_bool2])
print(b[b_bool1, b_bool2, b_bool3])

# 花式索引
print(b[[[0], [1, 2], [2, 3]]])
# ix_函数将若干一维整数数组转换为一个用于选取矩形区域的索引器
print(b[np.ix_([1, 0])])
print(b[np.ix_([1, 0], [2, 1])])
print(b[np.ix_([1, 0], [2, 1], [0, 3, 2])])

'''
数组切片是原始数组的视图, 与原始数组共享同一块数据存储空间
'''