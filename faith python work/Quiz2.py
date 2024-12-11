#Write a program that takes two numbers as inputs and displays their sum,product,difference and quotient
first_number = int(input("enter the first number: "))
second_number = int(input("enter the second number "))
sum = first_number + second_number
print(f"the sum of {first_number} and {second_number} is : {sum}")

product = first_number * second_number
print(f"the sum of {first_number} and {second_number} is : {product}")

difference = first_number - second_number
print(f"the difference of {first_number} and {second_number} is : {difference}")

quotient = first_number / second_number
print(f"the quotient of {first_number} and {second_number} is : {quotient}")

modulus = first_number % second_number
print(f"the modulus of {first_number} and {second_number} is : {modulus}")

floor_division = first_number // second_number
print(f"the floor_division of {first_number} and {second_number} is : {floor_division}")

division = first_number / second_number
print(f"the division of {first_number} and {second_number} is : {division}")


#Write a program that compares two integers and prints whether the first number is greater than,less than or equal to the second number.
first_number = int(input("enter the first_number: " ))
second_number = int(input("enter the second_number: "))
if first_number > second_number :
    print(f" {first_number} is greater than {second_number} ")
elif first_number < second_number :
    print(f" {first_number} is less than {second_number} ")
else :
    print(f" they are equal ")
    
    
##Write a program that checks if a given number is between 10 and 20 using logical operators(20 is inclussive)

number = int(input("enter a number: "))
if 10 <= number <= 20 :
    print(f"{number} is between 10 and 20")
else :
    print(f"{number} is not between 10 and 20")


#Write a program that prints the squares of all integers from 1-10 using a  loop

for i in range(1,11):
    print(i**2)


#Write a program that asks a user for their age,if the age is greater or equal to 18'print adult and you are qualified else you tell them you arenot qualified

age=int(input("enter age: "))
if age >= 18:
    print("adult and qualified")
else:
    print("not qualified")
    
    
#We have the  following student details and marks.Enter these details from the keyboard.
#student number=SEP23/BCS/14
#programiming=78
#data science=89
#computer application=55
#Calculate the average mark and print the answer in 3 decimal places


student_name = input("Enter the student name: ")
student_number = input("Enter the student number: ")
programiming_mark=int(input("Enter programming mark: "))
data_science_mark=int(input("Enter data science mark: "))
computer_application_mark=int(input("Enter computer application mark: "))
number_of_course_units = 3
total_mark= programiming_mark + data_science_mark + computer_application_mark / number_of_course_units
print(f"total mark is : {total_mark} ")
average_mark = total_mark / number_of_course_units                        
print(f"The average mark is : {average_mark:.3f} ")


#Write a program that converts c temp to f.The program should ask the user to enter the temp in c deg and then display the temp converted to f

celcius = float(input("Enter the temperature in celcius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"the temperature in fahrenheit is: {fahrenheit:.2f}")


#A cars miles per gallon can be calculated with the ff formula as written.
#mpg=milesdriven/gallons of gas used
#Write a program that asks the user for number of miles driven and gallons used and display the results

miles_driven = float(input("enter the number of miles driven: "))
gallons_used = float(input("enter the gallons of gas used: "))
mpg = miles_driven / gallons_used
print(f"the car's miles per gallon(MPG) is : {mpg:.2f}")


fahrenheit = (celcius * 9/5) + 32