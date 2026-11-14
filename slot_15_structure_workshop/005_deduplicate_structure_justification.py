raw_data=[("alice","delhi"),("bob","pune"),("alice","delhi")]
seen=set()
clean_records=[]
for record in raw_data:
    if record not in seen:
        seen.add(record)
        clean_records.append({"name":record[0],"city":record[1]})
print(clean_records)
        
