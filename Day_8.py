# Enter your code here. Read input from STDIN. Print output to STDOUT
#n = int(input())
# #name = []
# name = {}
# #name  = input()
# name2 = {}
# #name2  = input()
# for i in range (n):
#     name[i] = input()
# #    print (name[i])
# #    s = name.values()

# for l in range (n):
#     name2[l] = input()
# #    print (name[i])
# #    s = name.values()
# cop2 = {}
# for j in range (len(name)):
#     sep = name[j]
#     cop2[j] = sep.split(' ')
# #    print (cop2[j])

# for k in range (len(cop2)):
#     if cop2[k][0] == name2[k]:
#         print(cop2[k][0]+'='+cop2[k][1])
#     else:
#         print('Not found')


n = int(input())
d = {}
for i in range(n):
    x = input().split()
    d[x[0]] = x[1]
while True:
    try:
        name = input()
        if name in d:
            print(name, "=", d[name], sep="")
        else: 
            print("Not found")   
    except: 
        break






