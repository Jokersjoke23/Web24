def compare(x, y):
    if (x==1 and y==0) or (x==0 and y==1):
        res = 1
    else:
        res =0
    return res

x, y = map(int, input().split())
print(compare(x, y))