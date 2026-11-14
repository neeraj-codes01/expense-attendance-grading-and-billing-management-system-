# ask the user to enter items one at a time until they type 'done'
shopping_list=[]
item=input("enter item(or 'done' to finish):")
while item!="done":
    shopping_list.append(item)
    item=input("enter item(or 'done' to finish):")
print("your shopping list:",shopping_list)
print("total items:",len(shopping_list))