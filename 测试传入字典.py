test1 = {"a":1,"b":2,"c":3}

def test(ttt):
    for key,values in ttt.items():
        print(key+"的值是:"+str(values))

test(test1)