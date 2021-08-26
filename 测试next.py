a = [1,2,3,4,5]
b = a[0]
def fun():
    for i in a:
         yield i
for i in range(4):
    print(next(fun()))