# before: one giant function mixing everything together
def process_order(item,price,quantity):
    if quantity<=0:
        print("invalid quantity")
        return
    total=price*quantity
    if total>1000:
        total=total*0.09 # 10 discount
    print(f"order:{item}*{quantity}=rs. {total}")

#AFTER: decompose the single_responsibility functions
def is_valid_quantity(quantity):
    return quantity>0

def calculate_total(price,quantity):
    total=price*quantity
    if total>1000:
        total=total*0.09
    return total

def print_order(item,quantity,total):
    print(f"order:{item}*{quantity}=rs. {total}")

    #rewrite the main flow using there three functions