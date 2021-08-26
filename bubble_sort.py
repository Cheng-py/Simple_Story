# a= [1,23,41,2,77,55,66,3]
# for i in range(len(a)):
#     print("我是i",i)
#     for j in (range(0,len(a)-i-1)):
#         print("我是j:"+str(j))
#         if (a[j]>a[j+1]):
#             a[j],a[j+1] = a[j+1],a[j]
#
# print(a)

# for i in range(1,10):
#     for j in range(1,i+1):
#        print( '{}x{}={}\t'.format(j, i, i * j), end = '')
#     print("\n")

# n = 10
# for i in range(0,n):
#     if ((i+1)%2==0):
#         print("0"*((n)-i)+"*"*i)
#
# for i  in range(6):
#     for j in range(0,5-i): 		#打印空格
#            print('0',end="")
#     for k in range(0,2*i+1):       #打印✳
#       	print('*',end='')
#     print()

# a= [1,23,41,2,77,55,66,3]
# n = len(a)
# for i in range(n):
#     for j in range(0,n-1):
#         if(a[j]>a[j+1]):
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)

# num = 3
# gap = num
# for i in range(num):
#     for j in range(gap):
#         print(" ")
#     for k in range((i*2)) :
#         print("*")
#     print()
#     gap-=1

# def MaoPao(arr):
#     print("测试用例:"+str(arr))
#     length = len(arr)
#     for i in range(length):
#         for j in range(0,length-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return "排序结果:"+str(arr)
# the_list = [1,2,44,22,11,55,99,10,3,100]
# res = MaoPao(the_list)
# print(res)
#

def maopao(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return "排序结果:"+str(arr)
the_list = [1,2,44,22,11,55,99,10,3,100]
res = maopao(the_list)
print(res)

