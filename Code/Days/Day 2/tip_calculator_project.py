#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill_amount = input("What was the total bill? $")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
people_split = input("How many people to split the bill? ")
tip_percentage_modified = float("1." + tip_percentage)
split_amount = round((float(bill_amount) / int(people_split)) * tip_percentage_modified,2)
print(f"Each person should pay: ${split_amount:.2f}")