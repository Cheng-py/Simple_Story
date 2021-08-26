import os
a = "12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h12321312312312312312312312312312312412adhadadadasdhahdjkadadadqhhqiuh2u1u23h1h31723yh123123123h1u2h3h1"
b = list(a)
for i in range(len(b)):

    with open("test23.txt", "a", encoding="utf-8") as fp:
        if (i%50==0 and i!=0):
            fp.write("\n"+b[i])
        else:
            fp.write(b[i])


print(b)
# print("每输出十个数字换行，共计输出100个:")
# for num in range(1,100):#循环一百次
#     print("%3d" % num, end=" ")#不换行输出
#     if(num % 10 == 0):
#         print("")#换行输出