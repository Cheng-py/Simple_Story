def my_yield(n):
    for i in range(n):
        yield call(i)
        print("i=",i)

def call(i):
    return i*2

for m in my_yield(4):
    print("--------")
    print("m=",m)

