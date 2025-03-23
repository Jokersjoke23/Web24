n = int(input())
k = int(input())

for i in range(n + (n%2), k+1, 2):
    print(i, end=" ")