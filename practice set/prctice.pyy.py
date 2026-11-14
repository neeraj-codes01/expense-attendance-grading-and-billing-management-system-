complaints=["billing","services","billing","network","services","billing"]
frequency={}
for complaint in complaints:
    if complaint in frequency:
        frequency[complaint]+=1
    else:
        frequency[complaint]=1
print("frequency:",frequency)

distnict=set(complaints)
print(distnict)

most_frequent=max(frequency,key=frequency.get)
print(most_frequent)
print("count",frequency[most_frequent])

report=",".join(complaint.upper()for complaint in complaints)
print("report",report)

