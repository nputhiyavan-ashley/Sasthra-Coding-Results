n=int(input())
records = [input().strip() for _ in range(n)]
#code start first dictionary to hold the latest valid record for each unique id then split its components and validate the score, check if this id already has a record, compare updated_at to keep the most recent record, prepare the output list sorted by updated_at in ascending order, sort the output records by updated_at and return the output records
def func(n, records):
    latest_records = {}
    for record in records:
        id_str, name, score_str, updated_str = record.split(',')
        id = int(id_str)
        score = int(score_str)
        updated_at = int(updated_str)
        if 0 <= score <= 100:
            if id in latest_records:
                if updated_at > latest_records[id][2]:
                    latest_records[id] = (name, score, updated_at)
            else:
                latest_records[id] = (name, score, updated_at)
    # Here i have Prepared the output list sorted by updated_at in ascending order so that stores the output 
    output_records = []
    for id, (name, score, updated_at) in latest_records.items():
        output_records.append(f"{id},{name},{score},{updated_at}")
    output_records.sort(key=lambda x: int(x.split(',')[3]))
    return output_records 

    
    
