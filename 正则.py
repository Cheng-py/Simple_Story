import re
import time,datetime
from time import perf_counter,process_time
x_path = ""
a ='23hhjajdab程'
b = '123hjjek'
p = re.compile(r".[程]")
test = re.match(p,b,flags=0)
# print(test)

def fib(n):
#     if n<2:
#          return  n
#     else:
#          return  fib(n-2)+fib(n-1)
    a, b = 0, 1
    for _ in range(n):
        #编程习惯:如果循环对象在for当中没有用到,以_命名
        a, b = b, a + b
    return a


n=40
# t=time()
# print("计算结果：%d"%fib(n))
# print("计算%d个斐波那契数列和耗时：%f秒"%(n,(time()-t)))




# def fibiter(n):
#     a, b = 0, 1
#     for _ in range(n):
#         #编程习惯:如果循环对象在for当中没有用到,以_命名
#         a, b = b, a + b
#     return a
# n1=40
# t=datetime.datetime.now()
# print("计算结果：%d"%fibiter(n1))
# s = datetime.datetime.now()
# L = s-t
# print("计算%d个斐波那契数列和耗时：%s秒"%(n1,str(L)))
#
def fibiter(n):
    a, b = 0, 1
    for _ in range(n):
        #编程习惯:如果循环对象在for当中没有用到,以_命名
        a, b = b, a + b
    return a
t = time.process_time()
res = fibiter(40)
e = time.process_time()
print('result:',res)
print('Time consumed:',e-t)