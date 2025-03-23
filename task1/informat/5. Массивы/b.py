x = input().split()
a=[]
for i in range(len(x)):
    a.append(int(x[i]))

for i in range(len(a)):
    if a[i]%2==0:
        print(a[i], end=" ")