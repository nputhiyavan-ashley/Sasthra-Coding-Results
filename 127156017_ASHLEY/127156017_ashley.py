n=int(input())
meetings=[]
for _ in range(n):
    start,end=map(int,input().split())
    meetings.append((start,end))
starts=sorted(start for start,end in meetings)
ends=sorted(end for start,end in meetings)
i=j=0
rooms = 0
max_rooms = 0
while i<n:
    if starts[i]<ends[j]:
        rooms+=1
        max_rooms=max(max_rooms,rooms)
        i+=1
    else:
        rooms-=1
        j+=1
print(max_rooms)       
