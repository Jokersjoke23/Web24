x = input().split()
a=[]
for i in range(len(x)):
    a.append(int(x[i]))

c=0

for i in range(len(a)):
    if a[i]>0:
        c+=1
print(c)