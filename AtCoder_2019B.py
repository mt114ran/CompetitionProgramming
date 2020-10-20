# 2019B問題

N = int(input("日数を入力してください >>> "))

list = []
for i in range(N):
    list.append(int(input()))
    
for i in range(N-1):
    if list[i+1]==list[i]:
        print("stay")
    elif list[i+1]>list[i]:
        print("up [{}]".format(list[i+1]-list[i]))
    else:
        print("down [{}]".format(list[i]-list[i+1]))
