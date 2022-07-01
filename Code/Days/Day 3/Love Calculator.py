# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
full_name = name1.lower()+name2.lower()
T,R,U,E = full_name.count('t'),full_name.count('r'),full_name.count('u'),full_name.count('e')
true = T+R+U+E
L,O,V,E = full_name.count('l'),full_name.count('o'),full_name.count('v'),full_name.count('e')
love = L+O+V+E
true_love = int(str(true)+str(love))
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

