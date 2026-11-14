# bug1: index out of range
marks=[85,93,78]
print(marks[5]) #indexerror! only indices 0,1,2 exist
#bug2: off-by-one slicing confusion
marks=[82,92,78,88,95]
print(marks[1:3]) # beginner expects 3 items,but slicing stops before index 3
#actual output: [72,78] -- only 2 items (indices 1 and 2)
#fixes:
print(marks[2]) # big 1 fixed: valid index
print(marks[1:4])# bug 2 fixed: use index 4 to include index 3 as well