'''
python ������Ҫ�� utf-8 ����
��c\c++ ������ GB
����ע��
'''

# �����ʽ
# 1. %
'''
name = "woshishui"
phone = 123123
print("%s de dian hua shi %d" % (name, phone))
'''
# 2. {} �� .format()
# ���ƣ�����ȷ����������
# .format() �� format ��һ�������������������ַ����ĳ�Ա��������"awdawwaa".format();��Ϊһ������ǺϷ���
'''
n1 = input("���䰡�ݣ�")
n2 = 21312312
n3 = 213.13121
print("n1={} n2={} n3={}".format(n1, n2, n3))
'''

#pass ��ʾ����䣬��ʾ��ʱ�����������Ե�����һ����ǣ���Ҫ��������ɵĴ���
'''
score = 100
if score > 99:
    print("fa")
    pass #pass ����Ļس�������ֱ������ if ��ܡ��ǳ�����
    
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







#�ַ���

t = "abcdefghijklmnopqrstuvwxyz"
t2 = "    12312e1   "
t3 = "ab eda wrq w dqw dqw qwqw q"
t4 = "ADADaidAOIDJaiad wJDAJ A"
print("{}".format(t[1:10]))
print("{}".format(t[2:-1]))
print("{}".format(t[3:].capitalize())) #����ĸ���д
print("{}".format(t[3:].lower())) #ȫ����Сд
print("{}".format(t[3:].upper())) #ȫ�����д
print("{}".format(t3.title())) #ÿ����������ĸ���д
print("{}".format(t4.swapcase())) #��д��Сд��Сд���д
print("{}".format(t2.strip())) #ȥ����β�Ŀո�
print("{}".format(t2.lstrip())) #ȥ��ǰ���ֿո� ͬ��ȥ���󲿷ֿո� t2.rstrip()
print("res = {}".format(t2.find("123"))) #�����±�
print("res = {}".format(t2.find("12322"))) #�Ҳ������� -1
print("res = {}".format(t2.endswith(" "))) #�Ƿ���ʲô��β
print("res = {}".format(t2.startswith(" "))) #�Ƿ���ʲô��ͷ
print("cnt = {}".format(t2.count("1"))) #ͳ�Ƴ��ִ���
print("replace = {}".format(t2.replace("1", "x", 2))) #�� old �滻Ϊ new�����滻ǰ 2 ��
print("replace = {}".format(t2.replace("1", "x"))) #count Ϊ�ձ�ʾȫ���滻
print("join = {}".format("-".join(t3))) #ȡ�� text ���е��ʲ��� ������ ������









#�б�


lis = [1, 2, 3, 4, 5, 6, 1, "!@3", 1.02, "x", [2, 3, "?"], True]

lis[0] = "222" #֧�ֲ�ͬ���͵����ݵ��޸ĸ���
print("len = {}".format(len(lis))) #ʵ���� len() ���Ի�ȡ���������������͵ĳ���
del lis[0] #���в�������ɾ��Ԫ��
print(lis)
del lis[2 : 5] #����ɾ��
print(lis)
lis.remove("!@3") #ɾ��ָ��Ԫ��ֵΪ x ��Ԫ��
print(lis)
lis.pop(0) #ɾ��ָ���±� i ��Ԫ��
print(lis)
print("ind = {}".format(lis.index('x'))) #����ָ��Ԫ��ֵ��Ԫ���±�ֵ

print(lis[2])
print(lis[2 : 3]) #�±�Ϊ [2, 3) 
print(lis[:: -1]) #�����������ҿ�ʼ�������
print(lis * 3) #��� n ������

lis.append("das")
print(lis)
lis.append(["����һ���б�Ԫ��", 12, 213])
print(lis)
lis.insert(2, "����") # ���±�Ϊ 2 ��Ԫ��ǰ��������
print(lis)

lis1 = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lis1)
lis.extend("lis1") #��չ���������
print(lis)

#append �� extend �Ĳ��
lis.append("1234") #�������� "1234" һ������ӵ� lis ��
print(lis)
lis.extend("1234") #������"1234"ÿ��Ԫ��ȫ��������ӵ� lis ��
print(lis)

lis.reverse() #��ת�б�
print(lis)

lis2 = [21312, 32412,312,31,12,12,12,1 ,1]
lis2.sort() #����(�����б�ֻ��ͬ��������ʱ����)
print(lis2)






#Ԫ��


tupleA = (1, )

tuple1 = (1, "asdc", 2.121, [2, 3, 4])
print(tuple1[0])
print(tuple1[2 :])
print(tuple1[-2 : -1]) # ֻ�е���Ԫ��ʱ��� (2.121,) ������ź����Ź�ͬ˵�����Ǹ�Ԫ��
print(tuple1)
#����أ�Ԫ���ڵ��б�����޸�
tuple1[3][1] = "Y"
print(tuple1)
print("address = {}".format(id(tuple1))) # id() ��������ڴ��ַ
#for it in tuple1:
#    print(it, end = ' ')
tupleB = tuple(range(10))
print(tupleB)
print("cnt = {}".format(tupleB.count(8)))


# ����Ԫ��Ԫ�ظ�����
lis = ["123", 1]
dic = {"age" : "18"}
tuple1 = (100, "@", lis, dic)
tuple1[2][1] = "XX"
print(tuple1)
tuple1[3]["age"] = "30"
print(tuple1)














#�ֵ�

dict1 = {"name" : "limab", "age" : 30, "position" : "fuck"}

print(dict1)
print(len(dict1)) #��ֵ�Ը���
print(dict1["name"]) #��ֵ����
dict1["name"] = "sb" #��ֵ�޸�
print(dict1["name"])
print(dict1.keys()) #��ȡ���еļ�
print(dict1.values()) #��ȡ���е�ֵ
print(dict1.items()) #��ȡ���еļ�ֵ��
dict1.update({"new" : "new"}) #��ӻ��޸ļ�ֵ��
dict1.update({"age" : 18}) 
# �� dict1["new"] = "new" ͬ��
print(dict1)

#ͨ��ָ�� �� ��ɾ����ֵ��
del dict1["new"]
dict1.pop("position")
print(dict1)

dict1["n1"] = "12"
dict1["n2"] = "123"
dict1["n3"] = "123123"
dict1["age"] = "30"

# ����ǰ�᣺ͬ����
# ���� key ����
print(sorted(dict1.items(), key = lambda d : d[0]))
# ���� val ����
print(sorted(dict1.items(), key = lambda d : d[1]))
#����� key = ??? �� key ��ָ�������ݣ���ֵ������һ���������� lambda �ṩ��������
# lambda ��������:���ʽ  ����һ����������

for key, val in dict1.items():
    print("key : val = {} : {}".format(key, val))
    pass






#���з���

str1 = "abcde"
lis1 = [1, "@a$", list(range(20, 30))]
tuple1 = (3, "A")
dict1 = {"age" : "18", "name" : "Fuck"}
# �ϲ����� +
str2 = "XXSACX"
tuple2 = ("B", 4)
lis2 = list(range(100, 110))
print(str1 + str2)
print(tuple1 + tuple2)
print(lis1 + lis2)

# ���Ʋ��� *
# ʵ�ʾ��Ƕ�������� n �κϲ�����
print(str1 * 3)
print(tuple1 * 3)
print(lis1 * 3)

# �ж�Ԫ���Ƿ������������ in
# �����ֵ䣬�� �� ֵ�����Բ��Ҵ�����
print('a' in str1)
print(1 in lis1)
print("a" in tuple1)
print("age" in dict1)
print("18" in dict1)

















# ����

#ȱʡ������Ĭ��ֵ
def sum(a = 10, b = 10):
    print("sum = {}".format(a + b))
    pass

# �ɱ���� ��*args �� **kwargs ��ʵ�������ֿ��Բ��� args �� kwargs�������û��Զ���ģ��ص���ǰ����Ǻţ�
# args = arguments ����
# *args����ʾ�κζ����������������һ��Ԫ�顣������Ĳ�������δ֪���Ҳ���Ҫ֪����������ʱ����������һ���Ǽ�ֵ�ԵĿɱ������Ĳ����б��һ��������
# **kwargs����ʾ�ؼ��ֲ���������һ���ֵ䡣������Ĳ�������δ֪������Ҫ֪������������ʱ���Լ�ֵ�Ե���ʽ����������ƺͲ���ֵ��
# ע�⣺ͬʱʹ�� *args �� **kwargs ʱ���ڲ����б��б������� *args �� **kwargs ǰ�����򱨴�
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

# ���ִ��ݷ�ʽ
dic1 = {"a" : 10, "b" : "ASDFAW"}
Pri2(**dic1) #���ֵ������ǰ�� "**"
Pri2(a = 10, b = "ASDFAW") #���Ƽ�ֵ��

Pri3(1, 3, 45, 100) #��ʱ **kwargs Ϊ��
Pri3(name = "sb", age = 18) #��ʱ *args Ϊ��
Pri3(1, 3, 45, 100, name = "sb", age = 18)





# ��������(lambda) �൱��һ������ֵΪ������ʽ f(x) ����ĺ��������Դ� return f(x) ���
# �÷�:  f = lambda �����б�:���ʽ��Ȼ��ͨ�� f(�����б�) ������

f = lambda x, y : x + y
print(f(1, 3))




a = 1
print("���ǣ�" if a == 10 else "���ǣ�")
# �൱��
if a == 10:
    print("���ǣ�")
else:
    print("���ǣ�")

f = lambda x, y : x if x > y else y
print(f(1, 3))





print(any([0, 0, "", False]))


print(sorted(['a', 'C', 'g', 'F', 'Z', 'k', 'l', 'D', 'b', 'n', 'U'], key = str.lower)) # �ַ����޹ش�Сд��������
print(sorted(['a', 'C', 'g', 'F', 'Z', 'k', 'l', 'D', 'b', 'n', 'U'], key = str.upper)) # �ַ����޹ش�Сд��������
# str.lower��upper �����ַ������Сд���д����ַ�������˼�� sorted ���� key ���ţ���ȫ��Сд���д�����޹ش�Сд

lis = [1, 323, 23,13, 1223,12,321,235, 56]
lis.sort() # sort() ֱ���޸�ԭʼ�����޷���ֵ
print(lis)
lis.reverse() # �޷���ֵ
print(lis)



# zip() ���ص���һ�����������󣬸õ���������Ԫ�����У�ÿ��Ԫ��������ɵ�����������ͬλ�õ�Ԫ����ɡ�
# ��˿���ʹ���������е�����ת������Ҫ�������������ͣ������б��ֵ�ȣ���
print(list(zip([1, 2, 3], ['a', 'b', 'c'], ["abc", "bcd", "cdf"]))) #[(1, 'a', 'abc'), (2, 'b', 'bcd'), (3, 'c', 'cdf')]
print(*zip([1, 2, 3], ['a', 'b', 'c'], ["abc", "bcd", "cdf"])) #(1, 'a', 'abc') (2, 'b', 'bcd') (3, 'c', 'cdf')
# ����󣬿ɵ��������е�ÿ��Ԫ�ض��ᱻ��ֳɵ�����ֵ������˳����Ϊ������λ�ò������ݸ�����
print(*zip(*["abc", "bcd", "cdf"])) # ('a', 'b', 'c') ('b', 'c', 'd') ('c', 'd', 'f')



# enumerate()
lis = [1, "213!@#", 1.23923, 'c']

for index, val in enumerate(lis):
    print("id = {}, val = {}".format(index, val))
# id = 0, val = 1
# id = 1, val = 213!@#
# id = 2, val = 1.23923
# id = 3, val = c


# set �� set()
lis = [1, 23, 231, 23, 23]
set1 = set(lis)
set2 = set([1, 23, 123123])
# �����
print(set1.difference(set2)) 
print(set1 - set2)
# {231}

# ��������
print(set1.intersection(set2))
print(set1 & set2)
# {1, 23}

# ��������
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





class ������
    # ������
    a = '1'
    b = '2'

    # ���÷���
    def __init__(self) -> None:
        pass
    def __delattr__(self, __name: str) -> None:
        pass

    # ʵ������
    def ����1(self,�����б�):
        pass
    def ����2(self,�����б�):
        pass




# �ɰ� python ��д�� class Cat(object):
# python 3 ֮��Ͳ���Ҫ��ʽ��д������ object
class Cat:
    # ������
    # ���븽��������ֵ
    name = "c1"
    age = 0
    sex = '��'
    exist = False

    # ���÷���
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    
    def __init__(self, name = "c1", age = 0, sex = '��'):
        self.exist = True
        self.name = name
        self.age = age
        self.sex = sex
        print("һ�� Cat ���󱻹���")
        pass

    def __del__(self):
        print("һ�� Cat ��������")
        pass

    def __str__(self):
        return "һֻ{}è {}�����Ѿ� {} ����".format(self.sex, self.name, self.age)

    # ʵ������
    # ��ͬ���������ԣ������ڲ��ķ�������ʹ�� self ���ó�Ա����
    def f1(self):
        print(self.name) # ����ֱ�� print(name)
        pass

    def f2(self):
        print(self.age)
        pass
    
    def Intro(self):
        print("һֻ{}è {}�����Ѿ� {} ����".format(self.sex, self.name, self.age))
        pass


c1 = Cat()
c1.f1()
c1.f2()


c2 = Cat("Tom", 5, '��')
# ��ʱ����������������ͬ
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
# ��� C is called
# ��ϵͳ���� isCalled ������˳��Ϊ D -> B -> C -> A

print(D.__mro__) # ���������μ̳й�ϵ�������ൽ�������յ�Ĭ�ϳ��� object��
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
        # Creature.__init__(self, name) # ���¾��Ч
        super().__init__(name) # �Ӹ������Զ�Ѱ�ҿ�ִ�з��� __init__(self, name) �ĸ��࣬������ҵ��˸��� Creature�����������ʡ���� self
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
    # ������
    name = "abc"

    def __init__(self, age):
        self.age = age #ʵ������
        pass
    pass

stu = Student(18)

print(stu.name)
print(stu.age)

print(Student.name)
# print(Student.age) ����











import functools

def func(a, b, c, d):
    print(a + b + c + d)
    pass

func(1, 2, 3, 4)
newfunc1 = functools.partial(func, d = 100)
newfunc2 = functools.partial(func, c = 100, d = 10000)
# newfunc1() �̶����ݸ� func �� d ����ֵΪ 100
newfunc1(1, 2, 3)
# newfunc2() �̶����ݸ� func �� c ����ֵΪ 100��d ����ֵΪ 10000
newfunc2(100, 200, 300)

for i in range(2, 36):
    my_int = functools.partial(int, base = i)
    # �̶��� i ���Ʊ�ʾ�� 10000
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
    # op == 0 -> sum ����
    # op == 1 -> minus ����
    # op == 2 -> multiply ����
    
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



# ���غ����ıհ�
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

# ��Ϊ�ڰ� 3 ���������뵽 funcs �����б���ǰ��������
# ����1��Python�У���ѭ�������Ժ�ѭ�����е���ʱ���� i �������٣����Ǽ���������ִ�л�����
# ����2��Python�еĺ���ֻ���ڱ�����ʱ�ŻὫ�������ڵı���ֵȷ������
# ���ԣ����� f1��f2��f3 ��˵�����ǵ��õ� i ����ѭ�������� i ��ֵ 3������ǰ������Ļ����������ġ�



print(__f1())
print(__f2())
print(__f3())
# Output:
# 1
# 4
# 9

# ͨ���޸��ڲ��������壬����ס��ʱѭ����ÿ�� i ֵ
# ��ʱ���� __f1 ��˵���Ļ���Ϊ x = 1
# def f(x = 1): 
#     return x * x
# ͬ����� __f2 ��˵���Ļ���Ϊ x = 2
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



# ����ԭ��
ori = [0, 0]
# xOyƽ������ϵ�ϵ����ַ���
dir_x_positive = [1, 0]
dir_y_positive = [0, 1]
dir_x_negative = [-1, 0]
dir_y_negative = [0, -1]

def Point_create(setpos):
    pos = setpos.copy() # ����һ�������� setpos �б���ͬ�����б��������¿��ٵ��ڴ�ռ��У�
    # ��ֱ�� pos = setpos����ᵼ�´��������е㹲��ͬһ������� pos

    # direction ��ʾ�˶����򣨼�ĳ�����ϵĵ�λ���꣩
    # step ��ʾ�ڸ÷����ϵ��˶�����
    def Point_move(direction, step):
        nx = pos[0] + direction[0] * step
        ny = pos[1] + direction[1] * step
        # ����д�� pos = [nx, ny]���ᱻ���ɴ����µ���ʱ����
        pos[0] = nx
        pos[1] = ny
        return pos
    
    return Point_move

pt1 = Point_create(ori)
print(pt1(dir_x_positive, 10))  # ��1 �� x ���������� 10 ��   -- [10, 0]
print(pt1(dir_y_negative, 20))  # ��1 �� y �Ḻ������ 20 ��   -- [10, -20]

pt2 = Point_create(ori)
print(pt2(dir_x_negative, 100)) # ��2 �� x �Ḻ������ 100 ��  -- [-100, 0]
print(pt2(dir_y_positive, 50))  # ��2 �� y ���������� 50 ��   -- [-100, 50]





'''













































































































































































































































































































