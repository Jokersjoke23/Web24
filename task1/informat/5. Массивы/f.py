x = input().split()
a = []

for i in range(len(x)):
    a.append(int(x[i]))

c=0

for i in range(len(a) - 1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        c+=1
print(c)