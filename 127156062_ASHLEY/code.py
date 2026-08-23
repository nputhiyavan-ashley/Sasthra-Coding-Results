n = int(input())
dept = {}
ans=[]
for i in range(n):
    name,score= input().split(",")
    score= float(score)
    if name not in dept:
        dept[name] = []
    dept[name].append(score)
for name in dept:
    total= sum(dept[name])
    count= len(dept[name])
    avg= total / count
    maximum= max(dept[name])
    ans.append([name, avg, maximum])
ans.sort(key=lambda x: (-x[1], x[0]))

for name, avg, maximum in ans:
    if maximum.is_integer():
        maximum= int(maximum)

    print(f"{name}:{avg:.2f}:{maximum}")


    
