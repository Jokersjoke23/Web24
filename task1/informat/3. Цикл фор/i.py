x = int(input())
c = 0

for i in range(1, int(x**0.5) + 1):
    if x%i==0:
        if i*i==x:
            c+=1
        else:
            c+=2

print(c)
