# 2019C問題
# 6つの相異なる整数A,B,C,D,E,Fが与えられる。
# このうち,3番目に大きい数を調べるプログラムを作成せよ。

list = []

for i in range(6):
    list.append(int(input()))

for i in range(6):
    for s in range((6-i)-1):
        if list[s] < list[s+1]:
            m = list[s]
            list[s] = list[s+1]
            list[s+1] = m

print ("3番目に大きい数は {} です".format(list[2]))