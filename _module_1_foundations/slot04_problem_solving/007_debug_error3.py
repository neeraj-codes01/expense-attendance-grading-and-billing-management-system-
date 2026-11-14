# broken - runs without crashing,but gives the wrong answer
math=int(input("math marks:"))
english=int(input("english marks:"))
science=int(input("science marks:"))
average=(math+english)/3 # wrong! should include science
print(average)
#fixed
average=(math+english+science)/3
print(average)