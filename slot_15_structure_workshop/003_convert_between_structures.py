records=[("alice",22),("bob",21)]
records_as_dicts=[]
for name,age in records:
    d={"name":name,"age":age}
    records_as_dicts.append(d)
print(records_as_dicts)