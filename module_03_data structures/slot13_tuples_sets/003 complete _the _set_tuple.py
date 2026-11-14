def get_min_max(numbers):
    return(min(numbers),max(numbers))
low,high=get_min_max([4,8,1,9,3])
print("min:",low, "max:",high)

marks=[85,90,85,78,90,92]
unique_marks=set(marks)
print(unique_marks)