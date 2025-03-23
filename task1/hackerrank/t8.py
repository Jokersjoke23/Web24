n = int(input())  
arr = list(map(int, input().split()))  

max_score = max(arr)  
runner_up = None  

for x in arr:
    if x < max_score:
        if runner_up is None:
            runner_up = x  
        elif x > runner_up:
            runner_up = x  

print(runner_up)