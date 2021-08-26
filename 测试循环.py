list1=[1,2,3,4,5,6,7,8,9]
b = 'a,w,v,y,n,adadadwqgdg,aht'
list2 = list(b)
dict2 = dict(zip(list1,list2))
sum = 0
for key,values in dict2.items():
    sum+=1
    # print(type(values))

# dict1 = {"name":"test1","year":"18","sex":"m",}
# for (key,value) in dict1.items():
#     print("key:"+key+" "+"value:"+value)
# for key in dict1.keys():
# 	print(key+':'+dict1[key])
# for value in dict1.values():
#     print(value)

# dict1 = {'a':2,'e':3,'f':8,'d':4}
# res = sorted(dict1,reverse=True)
# print(res)
# dict2 = sorted(dict1)
dict1={'a':8,'b':4,'c':1,'d':2}
dict2 = sorted(dict1,key= lambda key:dict1[key])

print(dict2)