test=int(input())
if 1<=test and test <=10:
    for i in range(test):
        p=str(input())
        if 2 <= len(p) and len(p) <= 10000:
            print(p[::2], p[1::2])
else:
    print("Error")
