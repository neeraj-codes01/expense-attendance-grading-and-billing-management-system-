categories=["mobile","laptop","mobile","tablet","laptop","mobile"]
frequency={}
for category in categories:
    if category in frequency:
        frequency[category]+=1
    else:
        frequency[category]=1
print("frequency:",frequency)
dstnict=set(categories)
print(dstnict)
most_purchased=max(frequency,key=frequency.get)
print("most purchased",most_purchased)
print("count",frequency[most_purchased])
report=",," .join(c.upper() for c in categories)
print("report",report)