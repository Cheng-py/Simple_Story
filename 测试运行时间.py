import datetime
import time
def sum1(n):
    start_time = datetime.datetime.now()
    sum=0
    for x in range(1,n+1):
        # time.sleep(1)
        sum+=x
    end_time = datetime.datetime.now()
    print("递归用时 %s s" %(end_time-start_time))
    return sum

res=sum1(1 )