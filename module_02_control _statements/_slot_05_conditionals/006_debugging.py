# wrong: condition is reversed
marks=50
if marks<35:
    print("pass")
else:
    print("fail")
# task: identify the bug and fix it
# fixed:
if marks>=35:
    print("pass")
else:
    print("fail")