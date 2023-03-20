#Date:19.03.2023
#Topic: If-else Statement and ternary Operator


#write a prpgram if ticket pricing using if-else and ternary operator


#Using  if-else
age = input('Enter your age:')

# convert the string to int
your_age = int(age)

# determine the ticket price
# if your_age < 5:
#     ticket_price = 5
# elif your_age < 16:
#     ticket_price = 10
# else:
#     ticket_price = 18

# # show the ticket price
# print(f"You'll pay {ticket_price} for the ticket")


#Now Using ternary Operator
# syntax
# value_if_true if condition else value_if_false

# determine the ticket price
ticket_price=5 if your_age<5  else 18  if your_age<16 

# show the ticket price
print(f"You'll pay {ticket_price} for the ticket")