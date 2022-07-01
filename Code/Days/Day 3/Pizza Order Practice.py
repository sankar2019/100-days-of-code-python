# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    rate = 15
elif size == "M":
    rate = 20
elif size == "L":
    rate = 25
if (add_pepperoni == "N") and (extra_cheese == "N"):
    print(f"Your final bill is: ${rate}.")
elif (add_pepperoni == "Y") and (extra_cheese == "Y"):
    if (size=="S"):
        rate+=3
    elif (size=="M" or size=="L"):
        rate+=4
    print(f"Your final bill is: ${rate}.")
elif (add_pepperoni == "Y") and (extra_cheese == "N"):
    if (size=="S"):
        rate+=2
    elif (size=="M" or size=="L"):
        rate+=3
    print(f"Your final bill is: ${rate}.")
elif (add_pepperoni == "N") and (extra_cheese == "Y"):
    rate+=1
    print(f"Your final bill is: ${rate}.")