# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
#convert int to str
str_two_digit_number = str(two_digit_number)
first_num = str_two_digit_number[0]
second_num = str_two_digit_number[1]
first_num_int = int(first_num)
second_num_int = int(second_num)
sum_of_two = first_num_int + second_num_int
print(sum_of_two)
