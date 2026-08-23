n=int(input())
records={}
order=[]
rejected=0
valid_occurences=0
for _ in range(n):
    line=input().strip()
    id,name,email=line.split(",")
    id=id.strip()
    name=name.strip()
    email=email.strip().lower()
    if id=="" or email.count("@")!=1:
        rejected+=1
        continue
    before,after=email.split("@")
    if before=="" or after=="":
        rejected+=1
        continue      

    valid_occurences+=1
    if id not in records:
        order.append(id)
    records[id]=(id,name,email)    
duplicates_removed=valid_occurences-len(records)   
    record=records[id]
    print(record[0]+","+record[1]+","+record[2])
print("input:" +str(n))
print("valid:" +str(len(records)))
print("rejected:" +str(rejected))
print("duplicates_removed:" +str(duplicates_removed))  