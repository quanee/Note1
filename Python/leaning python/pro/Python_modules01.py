
"""
import
1.找到模块文件
    搜索查找模块文件
2.编译成位码(需要时)
    遍历模块搜索路径
    找到模块文件
    检查文件时间戳
        如果字节码文件比源代码文件旧,程序运行时就自动重新生成字节代码
        否则跳过
3.执行模块代码来创建其所定义的对象
    模块代码依次执行
    任何对变量名的赋值运算,都会产生所得模块文件的属性
"""


"""
模块搜索路径
1.程序主目录
    当前程序所在目录(最先搜索 可能覆盖其他目录同名模块)
2.PYTHONPATH目录(如果设置)
    环境变量设置的目录
3.标准链接库目录
    标准库安装在机器上的目录
4.任何.pth文件内容(如果存在)
    前面3个目录下存在的.pth文件内容所包含的目录
    过滤掉重复和不存在的
这4个共同组成sys.path
"""


"""
模块文件选择
 源代码文件xx.py
 字节码文件xx.pyc
 目录xx, 包导入
 编译扩展模块(C/C++),导入时动态链接(xx.so(Linux) xx.dll或xx.py(windows))
 用C编写好的内置模块, 并通过静态连接至Python
 ZIP文件组件, 导入时自动解压
 内存内映像, 对于frozen可执行文件
 Java类 在Jython版本的Python中
 .NET组件 在IronPython版本的Python中
"""

import time

print(time.__dict__)