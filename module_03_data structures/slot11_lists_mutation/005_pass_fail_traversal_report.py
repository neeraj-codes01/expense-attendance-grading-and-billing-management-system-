marks=[85,45,78,35,95,59,62]
passing=0
failing=0
for mark in marks:
    if mark>60:
        passing+=1
    else:
        failing+=1
print("passing",passing)
print("failing",failing)