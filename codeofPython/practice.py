'''
python 编译需要用 utf-8 运行
而c\c++ 可以用 GB
多行注释
'''

# 输出方式
# 1. %
'''
name = "woshishui"
phone = 123123
print("%s de dian hua shi %d" % (name, phone))
'''
# 2. {} 与 .format()
# 优势：不用确定数据类型
# .format() 中 format 是一个函数，可以是任意字符串的成员函数，如"awdawwaa".format();作为一个语句是合法的
'''
n1 = input("快输啊草：")
n2 = 21312312
n3 = 213.13121
print("n1={} n2={} n3={}".format(n1, n2, n3))
'''

#pass 表示空语句，表示暂时不作处理，可以当做是一个标记，是要过后来完成的代码
'''
score = 100
if score > 99:
    print("fa")
    pass #pass 语句后的回车键可以直接跳出 if 框架。非常方便
    
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("{} = {} * {}".format(row, col, row * col), end = " ")
        col += 1
        pass
    print()
    row += 1
    pass

for i in range(1, 100):#[1, 100)
    if i % 2 == 0:
        continue
    print("%d" % (i)) 
    pass

for ch in "123456789101112":
    print("{}".format(ch))


import random

for i in range(1, 100):
    x = random.randint(1, 100) # [1, 100]
    print("{}".format(x))







#字符串

t = "abcdefghijklmnopqrstuvwxyz"
t2 = "    12312e1   "
t3 = "ab eda wrq w dqw dqw qwqw q"
t4 = "ADADaidAOIDJaiad wJDAJ A"
print("{}".format(t[1:10]))
print("{}".format(t[2:-1]))
print("{}".format(t[3:].capitalize())) #首字母变大写
print("{}".format(t[3:].lower())) #全部变小写
print("{}".format(t[3:].upper())) #全部变大写
print("{}".format(t3.title())) #每个单词首字母变大写
print("{}".format(t4.swapcase())) #大写变小写，小写变大写
print("{}".format(t2.strip())) #去除首尾的空格
print("{}".format(t2.lstrip())) #去除前部分空格 同理去除后部分空格 t2.rstrip()
print("res = {}".format(t2.find("123"))) #返回下标
print("res = {}".format(t2.find("12322"))) #找不到返回 -1
print("res = {}".format(t2.endswith(" "))) #是否以什么结尾
print("res = {}".format(t2.startswith(" "))) #是否以什么起头
print("cnt = {}".format(t2.count("1"))) #统计出现次数
print("replace = {}".format(t2.replace("1", "x", 2))) #将 old 替换为 new，仅替换前 2 个
print("replace = {}".format(t2.replace("1", "x"))) #count 为空表示全部替换
print("join = {}".format("-".join(t3))) #取出 text 所有单词并用 ··· 来连接









#列表


lis = [1, 2, 3, 4, 5, 6, 1, "!@3", 1.02, "x", [2, 3, "?"], True]

lis[0] = "222" #支持不同类型的数据的修改覆盖
print("len = {}".format(len(lis))) #实际上 len() 可以获取三种序列数据类型的长度
del lis[0] #序列操作——删除元素
print(lis)
del lis[2 : 5] #批量删除
print(lis)
lis.remove("!@3") #删除指定元素值为 x 的元素
print(lis)
lis.pop(0) #删除指定下标 i 的元素
print(lis)
print("ind = {}".format(lis.index('x'))) #查找指定元素值的元素下标值

print(lis[2])
print(lis[2 : 3]) #下标为 [2, 3) 
print(lis[:: -1]) #负数步长从右开始逆序输出
print(lis * 3) #输出 n 次数据

lis.append("das")
print(lis)
lis.append(["加入一个列表元素", 12, 213])
print(lis)
lis.insert(2, "插入") # 在下标为 2 的元素前插入数据
print(lis)

lis1 = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lis1)
lis.extend("lis1") #拓展，批量添加
print(lis)

#append 和 extend 的差别
lis.append("1234") #仅将数据 "1234" 一整个添加到 lis 中
print(lis)
lis.extend("1234") #将序列"1234"每个元素全部批量添加到 lis 中
print(lis)

lis.reverse() #翻转列表
print(lis)

lis2 = [21312, 32412,312,31,12,12,12,1 ,1]
lis2.sort() #排序(仅对列表只有同类型数据时有用)
print(lis2)






#元组


tupleA = (1, )

tuple1 = (1, "asdc", 2.121, [2, 3, 4])
print(tuple1[0])
print(tuple1[2 :])
print(tuple1[-2 : -1]) # 只有单个元素时输出 (2.121,) 这个逗号和括号共同说明他是个元组
print(tuple1)
#特殊地，元组内的列表可以修改
tuple1[3][1] = "Y"
print(tuple1)
print("address = {}".format(id(tuple1))) # id() 输出数据内存地址
#for it in tuple1:
#    print(it, end = ' ')
tupleB = tuple(range(10))
print(tupleB)
print("cnt = {}".format(tupleB.count(8)))


# 讨论元组元素更改性
lis = ["123", 1]
dic = {"age" : "18"}
tuple1 = (100, "@", lis, dic)
tuple1[2][1] = "XX"
print(tuple1)
tuple1[3]["age"] = "30"
print(tuple1)














#字典

dict1 = {"name" : "limab", "age" : 30, "position" : "fuck"}

print(dict1)
print(len(dict1)) #键值对个数
print(dict1["name"]) #键值查找
dict1["name"] = "sb" #键值修改
print(dict1["name"])
print(dict1.keys()) #获取所有的键
print(dict1.values()) #获取所有的值
print(dict1.items()) #获取所有的键值对
dict1.update({"new" : "new"}) #添加或修改键值对
dict1.update({"age" : 18}) 
# 与 dict1["new"] = "new" 同理
print(dict1)

#通过指定 键 来删除键值对
del dict1["new"]
dict1.pop("position")
print(dict1)

dict1["n1"] = "12"
dict1["n2"] = "123"
dict1["n3"] = "123123"
dict1["age"] = "30"

# 排序前提：同类型
# 按照 key 排序
print(sorted(dict1.items(), key = lambda d : d[0]))
# 按照 val 排序
print(sorted(dict1.items(), key = lambda d : d[1]))
#这里的 key = ??? 的 key 是指排序依据，右值必须是一个函数，而 lambda 提供匿名函数
# lambda 参数名称:表达式  创建一个匿名函数

for key, val in dict1.items():
    print("key : val = {} : {}".format(key, val))
    pass






#公有方法

str1 = "abcde"
lis1 = [1, "@a$", list(range(20, 30))]
tuple1 = (3, "A")
dict1 = {"age" : "18", "name" : "Fuck"}
# 合并操作 +
str2 = "XXSACX"
tuple2 = ("B", 4)
lis2 = list(range(100, 110))
print(str1 + str2)
print(tuple1 + tuple2)
print(lis1 + lis2)

# 复制操作 *
# 实质就是对自身进行 n 次合并操作
print(str1 * 3)
print(tuple1 * 3)
print(lis1 * 3)

# 判断元素是否存在于序列中 in
# 对于字典，键 和 值都可以查找存在性
print('a' in str1)
print(1 in lis1)
print("a" in tuple1)
print("age" in dict1)
print("18" in dict1)

















# 函数

#缺省参数的默认值
def sum(a = 10, b = 10):
    print("sum = {}".format(a + b))
    pass

# 可变参数 ：*args 和 **kwargs （实际上名字可以不是 args 或 kwargs，这是用户自定义的，重点是前面的星号）
# args = arguments 参数
# *args：表示任何多个无名参数，它是一个元组。当传入的参数个数未知，且不需要知道参数名称时，用来发送一个非键值对的可变数量的参数列表给一个函数。
# **kwargs：表示关键字参数，它是一个字典。当传入的参数个数未知，但需要知道参数的名称时，以键值对的形式传入参数名称和参数值。
# 注意：同时使用 *args 和 **kwargs 时，在参数列表中必须满足 *args 在 **kwargs 前，否则报错
def Pri1(*args):
    print(args)
    pass

def Pri2(**kwargs):
    print(kwargs)
    pass

def Pri3(*args, **kwargs):
    print(args)
    print(kwargs)
    pass


sum()

Pri1(1, 2, 2, 32,2 ,3, "!@312", [123,213,"@3"], (True, "IKJOI"), "---")

# 两种传递方式
dic1 = {"a" : 10, "b" : "ASDFAW"}
Pri2(**dic1) #给字典变量名前加 "**"
Pri2(a = 10, b = "ASDFAW") #类似键值对

Pri3(1, 3, 45, 100) #此时 **kwargs 为空
Pri3(name = "sb", age = 18) #此时 *args 为空
Pri3(1, 3, 45, 100, name = "sb", age = 18)





# 匿名函数(lambda) 相当于一个返回值为后面表达式 f(x) 结果的函数，即自带 return f(x) 语句
# 用法:  f = lambda 参数列表:表达式，然后通过 f(参数列表) 来调用

f = lambda x, y : x + y
print(f(1, 3))




a = 1
print("你是？" if a == 10 else "我是？")
# 相当于
if a == 10:
    print("你是？")
else:
    print("我是？")

f = lambda x, y : x if x > y else y
print(f(1, 3))





print(any([0, 0, "", False]))


print(sorted(['a', 'C', 'g', 'F', 'Z', 'k', 'l', 'D', 'b', 'n', 'U'], key = str.lower)) # 字符串无关大小写进行排序
print(sorted(['a', 'C', 'g', 'F', 'Z', 'k', 'l', 'D', 'b', 'n', 'U'], key = str.upper)) # 字符串无关大小写进行排序
# str.lower或upper 返回字符串变成小写或大写后的字符串，意思是 sorted 按照 key 来排，就全是小写或大写，即无关大小写

lis = [1, 323, 23,13, 1223,12,321,235, 56]
lis.sort() # sort() 直接修改原始对象，无返回值
print(lis)
lis.reverse() # 无返回值
print(lis)



# zip() 返回的是一个迭代器对象，该迭代器生成元组序列，每个元组由输入可迭代对象中相同位置的元素组成。
# 因此可以使用它来进行迭代或转换成需要的其他数据类型（例如列表、字典等）。
print(list(zip([1, 2, 3], ['a', 'b', 'c'], ["abc", "bcd", "cdf"]))) #[(1, 'a', 'abc'), (2, 'b', 'bcd'), (3, 'c', 'cdf')]
print(*zip([1, 2, 3], ['a', 'b', 'c'], ["abc", "bcd", "cdf"])) #(1, 'a', 'abc') (2, 'b', 'bcd') (3, 'c', 'cdf')
# 解包后，可迭代对象中的每个元素都会被拆分成单独的值，并按顺序作为单独的位置参数传递给函数
print(*zip(*["abc", "bcd", "cdf"])) # ('a', 'b', 'c') ('b', 'c', 'd') ('c', 'd', 'f')



# enumerate()
lis = [1, "213!@#", 1.23923, 'c']

for index, val in enumerate(lis):
    print("id = {}, val = {}".format(index, val))
# id = 0, val = 1
# id = 1, val = 213!@#
# id = 2, val = 1.23923
# id = 3, val = c


# set 与 set()
lis = [1, 23, 231, 23, 23]
set1 = set(lis)
set2 = set([1, 23, 123123])
# 差集操作
print(set1.difference(set2)) 
print(set1 - set2)
# {231}

# 交集操作
print(set1.intersection(set2))
print(set1 & set2)
# {1, 23}

# 并集操作
print(set1.union(set2))
print(set1 | set2)
# {1, 123123, 23, 231}

lis = [1, 23, 231, 23, 23]
set1 = set(lis)
print(set1)

set1.remove(1)
print(set1)
set1.discard(23)
print(set1)





class 类名：
    # 类属性
    a = '1'
    b = '2'

    # 内置方法
    def __init__(self) -> None:
        pass
    def __delattr__(self, __name: str) -> None:
        pass

    # 实例方法
    def 方法1(self,参数列表):
        pass
    def 方法2(self,参数列表):
        pass




# 旧版 python 的写法 class Cat(object):
# python 3 之后就不需要显式地写出参数 object
class Cat:
    # 类属性
    # 必须附带空属性值
    name = "c1"
    age = 0
    sex = '雄'
    exist = False

    # 内置方法
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    
    def __init__(self, name = "c1", age = 0, sex = '雄'):
        self.exist = True
        self.name = name
        self.age = age
        self.sex = sex
        print("一个 Cat 对象被构造")
        pass

    def __del__(self):
        print("一个 Cat 对象被销毁")
        pass

    def __str__(self):
        return "一只{}猫 {}，它已经 {} 岁了".format(self.sex, self.name, self.age)

    # 实例方法
    # 不同于其他语言，在类内部的方法必须使用 self 引用成员属性
    def f1(self):
        print(self.name) # 不能直接 print(name)
        pass

    def f2(self):
        print(self.age)
        pass
    
    def Intro(self):
        print("一只{}猫 {}，它已经 {} 岁了".format(self.sex, self.name, self.age))
        pass


c1 = Cat()
c1.f1()
c1.f2()


c2 = Cat("Tom", 5, '雌')
# 此时以下两句输出结果相同
print(c2)
c2.Intro()


class Animal:
    def walk(self):
        print("A {} is walking now".format(type(self)))
    pass

class Cat(Animal):
    def meow(self):
        print("Cat Meow")
    pass

class Dog(Animal):
    def bark(self):
        print("Dog Bark")
    pass


c = Cat()
d = Dog()
c.meow()
d.bark()
c.walk()
d.walk()

Cat Meow
Dog Bark
A <class '__main__.Cat'> is walking now
A <class '__main__.Dog'> is walking now


class Creature:
    name = ""
    exist = True
    def isExist(self):
        print("{} is existed".format(self.name))
    def setName(self, nm):
        self.name = nm
    pass

class Animal:
    def walk(self):
        print("A {} is walking now".format(type(self)))
    pass

class Cat(Animal, Creature):
    def meow(self):
        print("Cat Meow")
    pass

class Dog(Animal, Creature):
    def bark(self):
        print("Dog Bark")
    pass


c = Cat()
d = Dog()
c.setName("Cat1")
d.setName("Dog1")
c.isExist()
d.isExist()
# Cat1 is existed
# Dog1 is existed






class A:
    def isCalled(self):
        print("A is called")
    pass
class B(A):
    pass
class C(A):
    def isCalled(self):
        print("C is called")
    pass
class D(B, C):
    pass

d = D()
d.isCalled()
# 输出 C is called
# 故系统查找 isCalled 方法的顺序为 D -> B -> C -> A

print(D.__mro__) # 输出类的依次继承关系（从子类到父类最终到默认超类 object）
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)


class Creature:
    name = ""
    exist = True
    def __init__(self, name):
        self.name = name;
        pass
    def isExist(self):
        print("{} is existed".format(self.name))
    def setName(self, nm):
        self.name = nm
    pass

class Animal:
    def walk(self):
        print("A {} is walking now".format(type(self)))
    pass

class Cat(Animal, Creature):
    def __init__(self, name):
        # Creature.__init__(self, name) # 与下句等效
        super().__init__(name) # 从父类中自动寻找可执行方法 __init__(self, name) 的父类，这里就找到了父类 Creature，且这里参数省略了 self
        pass
    def meow(self):
        print("Cat Meow")
    pass

class Dog(Animal, Creature):
    def bark(self):
        print("Dog Bark")
    pass


c = Cat("Cat1")
d = Dog("Dog1")
c.isExist()
d.isExist()




class Student:
    # 类属性
    name = "abc"

    def __init__(self, age):
        self.age = age #实例属性
        pass
    pass

stu = Student(18)

print(stu.name)
print(stu.age)

print(Student.name)
# print(Student.age) 报错











import functools

def func(a, b, c, d):
    print(a + b + c + d)
    pass

func(1, 2, 3, 4)
newfunc1 = functools.partial(func, d = 100)
newfunc2 = functools.partial(func, c = 100, d = 10000)
# newfunc1() 固定传递给 func 的 d 参数值为 100
newfunc1(1, 2, 3)
# newfunc2() 固定传递给 func 的 c 参数值为 100，d 参数值为 10000
newfunc2(100, 200, 300)

for i in range(2, 36):
    my_int = functools.partial(int, base = i)
    # 固定以 i 进制表示数 10000
    print(my_int('10000'))
    pass




def cal(a, b, FunctionKey):
    print(FunctionKey(a, b))
    pass

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def mypow(a, b):
    return a ** b

lis = [plus, minus, multiply, mypow]
a, b = 2, 10

for func in lis:
    cal(a, b, func)
    pass

# Output: 
# 12
# -8
# 20
# 1024



def cal(op):
    # op == 0 -> sum 操作
    # op == 1 -> minus 操作
    # op == 2 -> multiply 操作
    
    def sum(*arg):
        res = 0
        for i in arg:
            res += i
        return res

    def minus(*arg):
        res = arg[0]
        for i in arg[1 : ]:
            res -= i
        return res

    def multiply(*arg):
        res = 1
        for i in arg:
            res *= i
        return res
    
    lis = [sum, minus, multiply]
    
    return lis[op]
    

a, b, c = 2, 5, 10

for i in range(0, 3):
    func = cal(i)
    print(func(a, b, c))
    pass

# Output:
# 17
# -13
# 100






lis = [{"name" : "abc", "age" : 18}, {"name" : "cde", "age" : 68}, {"name" : "def", "age" : 39}, {"name" : "fgh", "age" : 11}]

print(sorted(lis, key = lambda x : x["name"]))
# Output: [{'name': 'abc', 'age': 18}, {'name': 'cde', 'age': 68}, {'name': 'def', 'age': 39}, {'name': 'fgh', 'age': 11}]

print(sorted(lis, key = lambda x : x["age"]))
# Output: [{'name': 'fgh', 'age': 11}, {'name': 'abc', 'age': 18}, {'name': 'def', 'age': 39}, {'name': 'cde', 'age': 68}]



# 返回函数的闭包
def myPower(exp = 1):
    def cal(x):
        return x ** exp
    return cal

pow2, pow3, pow4 = myPower(2), myPower(3), myPower(4)

num = 4
print("{a}^2 = {}, {a}^3 = {}, {a}^4 = {}".format(pow2(num), pow3(num), pow4(num), a = num))
# Output: 4^2 = 16, 4^3 = 64, 4^4 = 256


def count():
    funcs = []
    for i in range(1, 4):
        def f():
            return i * i
        funcs.append(f)
    return funcs

def __count():
    funcs = []
    for i in range(1, 4):
        def f(x = i): 
            return x * x
        funcs.append(f)
    return funcs


func_lis = count()
f1, f2, f3 = func_lis[0], func_lis[1], func_lis[2]


__func_lis = __count()
__f1, __f2, __f3 = __func_lis


print(f1())
print(f2())
print(f3())
# Output:
# 9
# 9
# 9

# 因为在把 3 个函数加入到 funcs 函数列表中前，发生了
# 现象1：Python中，当循环结束以后，循环体中的临时变量 i 不会销毁，而是继续存在于执行环境中
# 现象2：Python中的函数只有在被调用时才会将函数体内的变量值确定下来
# 所以，对于 f1、f2、f3 来说，它们调用的 i 都是循环结束后 i 的值 3，即当前作用域的环境所决定的。



print(__f1())
print(__f2())
print(__f3())
# Output:
# 1
# 4
# 9

# 通过修改内部函数定义，保留住当时循环的每个 i 值
# 此时对于 __f1 来说它的环境为 x = 1
# def f(x = 1): 
#     return x * x
# 同理对于 __f2 来说它的环境为 x = 2
# def f(x = 2): 
#     return x * x






def func():
    a = 1
    def count():
        nonlocal a
        a = a + 1
        return a
    
    return count

f = func()
print(f())
# Output: 2



# 坐标原点
ori = [0, 0]
# xOy平面坐标系上的四种方向
dir_x_positive = [1, 0]
dir_y_positive = [0, 1]
dir_x_negative = [-1, 0]
dir_y_negative = [0, -1]

def Point_create(setpos):
    pos = setpos.copy() # 复制一个内容与 setpos 列表相同的新列表（存在于新开辟的内存空间中）
    # 若直接 pos = setpos，则会导致创建的所有点共用同一个坐标点 pos

    # direction 表示运动方向（即某方向上的单位坐标）
    # step 表示在该方向上的运动距离
    def Point_move(direction, step):
        nx = pos[0] + direction[0] * step
        ny = pos[1] + direction[1] * step
        # 不能写成 pos = [nx, ny]，会被当成创建新的临时变量
        pos[0] = nx
        pos[1] = ny
        return pos
    
    return Point_move

pt1 = Point_create(ori)
print(pt1(dir_x_positive, 10))  # 点1 在 x 轴正方向走 10 步   -- [10, 0]
print(pt1(dir_y_negative, 20))  # 点1 在 y 轴负方向走 20 步   -- [10, -20]

pt2 = Point_create(ori)
print(pt2(dir_x_negative, 100)) # 点2 在 x 轴负方向走 100 步  -- [-100, 0]
print(pt2(dir_y_positive, 50))  # 点2 在 y 轴正方向走 50 步   -- [-100, 50]





'''













































































































































































































































































































