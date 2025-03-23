x = input().split()
a=[]
for i in range(len(x)):
    a.append(int(x[i]))

for i in range(1, len(a)):
    if a[i]>a[i-1]:
        print(a[i], end=" ")