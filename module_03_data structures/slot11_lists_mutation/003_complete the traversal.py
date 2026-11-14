#complete: sum all marks using a traversal loops
marks=[83,92,78,88,95]
total=0
for mark in marks:
    total=total+mark
print("total:",total)

# complete: count how many marks are>=90
high_count=0
for mark in marks:
    if mark>=90:
        high_count=high_count+1
print("high_count:",high_count)