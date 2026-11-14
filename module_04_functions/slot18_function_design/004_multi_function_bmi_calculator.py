def get_weight_height():
    #get and calculate weight (kg) and height (m) from user.""
    weight=float(input("enter weight(kg)"))
    height=float(input("enter height(m)"))
    return weight,height

def calculate_bmi(weight,height):
    #calculate bmi from height and weight.
    return weight/(height**2)
def classify_bmi(bmi):
    #return a bmi category label.""
     if bmi < 18.5:
        return("underweight")
     elif bmi < 25:
        return("normal")
     else:
        return("underweight")

weight,height=get_weight_height()
bmi=calculate_bmi(weight,height)
category=classify_bmi(bmi)
print(f"bmi:{bmi} category:{category}")