# def f1(x):
#     return x+1
# a  = [0,1,2,3,4,]
# b  =map(f1,a)
# print(b)
# print(list(b))
#
# print(list(map(lambda x:x.upper(),"abcdef")))

# def f1(x):
#     return str.isupper(x)
#
# l1 = ['a','b','c','D','E','F']
#
# list1 = filter(f1,l1)
# print(list1)
# print(list(list1))
# print(list(filter(lambda x:str.isupper(x),l1)))

# from functools import reduce
# nums =[1,2,3,4]
# print(reduce(lambda x,y:x*y,nums,1))
# sequence

# a= ['a','b','c','e','f']
# b=[1,2,3,4,5]
# print(list(zip(a,b)))

# a=('a','b','c','e','f',)
# b =(1,2,3,4,5,)
# # c = *b
# print(type(*b))
# print(*c)
# L1 = ['a','b','c','e','f']
# L2 = [1,2,3,4,5]
# L3 = dict(zip(L1,L2))
# print(L3)
# functions=[ lambda x,i=i: x*i for i in range(1,9)]
# for function in functions:
#     print(function(3))

res = [x*y for x in range(10) if x > 2 for y in range(1,4) if y < 3]
print(res)

list1 = []
for x in range(10):
    if x > 8:
        for y in range(5):
            if (x-y) > 0:
               list1.append(x-y)

print(list1)
res = [x-y for x in range(10) if x > 7 for y in range(5) if y < 3]
print(res)
res = [x-y for x in range(10) if(x>8) for y in range(5) if (x-y) > 0]
print(res)