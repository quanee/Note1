
# 计算嵌套子列表结构中所有数字的总和
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


L = [1, [2, 3, [4, 5]]]
print(sumtree(L))