# -*- coding:utf-8 -*-
#整数、浮点数、字符串、布尔值、空值None、列表、字典、集合
print(type(int('11111')))
print(type(11111111111111111111111))
print(type(11111111111.11111111111111111111))
print(4/2,9/3)

print(r'''i'am ok "{a}\t \\\\''' . format(a = 5)) #r表示不转义看到是啥就是啥
# 在计算机内存中，str统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就编码为UTF-8编码。
print('123文档')
print(b'\xe4\xb8\xad'.decode('utf-8').encode('utf-8'))#byte类型的每个字符都只占用一个字节。传输、保存到文件的类型
print(b'123\xe6\x96\x87\xe6\xa1\xa3'.decode('utf-8'))
print(b'123\xe6\x96\x87\xe6\xa1\xe6\x96\x87'.decode('utf-8', errors='ignore'))#忽略部分错误
print(type('中文'))
print(len('中文'))#字节数 6
str = 'abc'
print(str.replace("a","AB"))
print(str)
print("  ss   ".strip()) #ss


print(type(True),type(False))   #and or not
print(type(None))
list1 = [4,1,2,5,-8]    #有序
print(type(list1))
print(len(list1))
list1.insert(1,'insert')
list1.append('append')
print(list1)
print(list1.pop())  #append
arr = [2,-9,5,1]
arr.sort()
print(arr)

dict1 =  {'name':'覃佳','age':18}
print(type(dict1))
print(dict1['name'])
print('name' in dict1)
print('sex' in dict1)
print(dict1.get('name'))
print(dict1.get('sex',-1))
del dict1['name']
print(dict1)
print(dict1.pop('age'))
print(dict1)

print(set([5,5,1,1,2,2,3,4]))#唯一、无序

age = 6
if age > 18:
    print('adult')
elif age > 6:
    print('teenager')
else:
    print('kid')

sum = 0
for i in range(0,101):
    sum += i
print(sum)
print(type(range(1,100)))

sum = 0
n = 0
while n < 10:
    n += 1
    print(n)
    if n > 7:
        break
    if n % 2 == 0:
        continue
    sum += n
print(n)
print("///",sum,n)



