#These determine the order in which a program can be executed basing on loops or conditions.
#They also specify the flow of a program. 
###Conditional Statements
#These always execute if a condition is true/false.
#They use else and ifelse.

#Write a program that asks a user for the food type bought from the mkt.The program should print bought chicken if the user enters chicken,liver if the user enterts liver,else fish
food_type = input("Enter the food type bought: ").lower()
if food_type == 'Chicken':
    print("You bought chicken from the market.")
elif food_type == 'Liver':
    print("You bought liver from the market.")
else:
    print("You bought fish from the market.")