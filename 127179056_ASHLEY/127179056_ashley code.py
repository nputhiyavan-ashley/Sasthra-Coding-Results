lines = ["id,name,score", "1,Ana,80", "2,,90", "3,Cia,NULL"]
header = lines[0].split(",")
rows = lines[1:]
total = len(rows)
missing = [0] * len(header)
for row in rows:
    values = row.split(",")
    for i in range(len(header)):
      if i > len(values) and values[i] == "" or values[i] == "NULL":
          missing[i] +=1

for i in range(len(header)):
   valid = total -missing[i]
   if total == 0:
       percentage = 0.00
   else:
        percentage = (valid / total) * 100
   print(f"{header[i]}:{missing[i]}:{percentage:.2f}")

   
        
