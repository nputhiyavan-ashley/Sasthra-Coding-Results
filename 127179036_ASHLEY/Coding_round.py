
n=int(input())
all_dept={}
for _ in range(n):
    detail=input()
    detail=detail.split(",")
    dept,score=detail[0],detail[1]
    if dept not in all_dept:
        all_dept[dept]=[score]
    else:
        all_dept[dept].append(score)
depts=sorted(list(all_dept.keys()))
max_score=[]
avg_score=[]
for dept in depts:
    max_score.append(max(all_dept[dept]))
    term_sum=0
    for i in all_dept[dept]:
        term_sum+=float(i)
    avg=term_sum/len(all_dept[dept])
    avg_score.append(round(avg,2))
for i in range(len(depts)):
    print(f"{depts[i]}:{avg_score[i]}:{max_score[i]}")
    
