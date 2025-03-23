x = input().split()
a = []

for i in range(len(x)):
    a.append(int(x[i]))

max=a[0]
c=0

for i in range(1, len(a)):
    if a[i]>max:
        max=a[i]
        c=i
print()