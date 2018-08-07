# -*- coding:utf-8 -*-
# 函数、递归、闭包、装饰器
#默认参数、可变参数、关键字参数
#对象、模块

def f1(name,age,**kw):
    print(name,age,kw)

f1('覃佳',18,sex='girl')

def digui(n):
    if n == 1:
        return 1
    return n * digui(n-1)
print(digui(3))