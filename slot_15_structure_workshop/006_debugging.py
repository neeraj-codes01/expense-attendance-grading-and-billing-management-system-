# broken: using a list to check membership repeatedly is slow and all duplicates
registered_users=[]
registered_users.append("alice123")
registered_users.append("alice123")# oops -- duplicate allowed,no warning
print(registered_users) #--wrong
#fixed: use a set,which enforces uniqueness automatically
registered_users=set()
registered_users.add("alice123")
registered_users.add("alice123")#ignored
print(registered_users)