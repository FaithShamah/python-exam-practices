##1.write a python function named "calculate_area" that takes the radius of a circle as a parameter and returns the 
# area of the circle. Use the formula : area = pie*r^2 (Assume that pie = 3.14), test the function with a radius of 5.
def calculate_area(radius):
    pie = 3.14
    area = pie * (radius ** 2)
    return area

radius = 5
result = calculate_area(radius)
print(f"The radius of circle with radius {radius} is:{result}")

##2.write a recursive function to calculate the sum of natural numbers up to n.Test the function with n=4
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
 
n = 4
result = sum_of_natural_numbers(n)
print(f"The sum of natural numbers up to {n} is : {result}")

##3.given the list below, remove the element at index 2 and insert the value 10 at at the end. numbers = [1,3,5,7,9]
numbers = [1,3,5,7,9]

numbers.pop(2)

numbers.append(10)

print(numbers)

##4.Using list comprehension,create a new list that contains only even numbers from the original list.
even_numbers = [2,4,6,8,10]

filtered_even_numbers = [num for num in even_numbers if num % 2 == 0]

print(filtered_even_numbers)

##5.Given the dctionary below,update the value of 'age'  to 25 and add a new key value pair ('city','NewYork') 
# student_info={'name':Alice,'age':20,'grade':A}
student_info = {'name' : 'Alice' , 'age' : '20' , 'grade' : 'A'}
student_info['age'] = 25
student_info['city'] = 'NewYork'
print(student_info)

##6.Using dictionary comprehension , create a new dictionary with only key value pairs where the value is 
# greater than 5. original_dic = {'a':3,'b':8,'c':2,'d':7}
original_dic = {'a':3,'b':8,'c':2,'d':7}
new_dic = {key: value for key,value in original_dic.items() if value > 5}
print(new_dic)

#Write a python snippet that asks the user for their age and prints "You are eligible" if age is greater than
# or equal to 18 ,otherwise prints "You are not eligible".

age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligible")

else:
    print("You are not eligible")

#a)Write a python function named "grade_students" that takes a student's mark  as input and returns their corresponding 
# grade based on the following criteria: 90 or above: 'A' ,80-89:'B' ,70-79:'C' ,60-69:'D', Below 60 :'F', b)Test the 
# function with a mark of 85,c) Modify the "grade_students" function to handle the case where the input mark is not a 
# valid number, the function should return "InvalidInput." Test the function with both a valid mark and an invalid input.
# d)Enhance the "grade_students" function to also provide a message along with the grade: 'Excellent' for grades 'A' and 
# 'B' ,'Good' for grade 'C' 'Satisfactory' for grade 'D' 'Needs Improvement' for grade 'F'. e)The function should now 
# return both the grade and the corresponding message . Test the function with a mark of 78.

#a)
def grade_students(mark):
    if mark >=90:
        return 'A'
    elif mark >=80:
        return 'B'
    elif mark >=70:
        return 'C'
    elif mark >=60:
        return 'D'
    else:
        return 'F'
    
 #b
 
mark = 85
grade = grade_students(mark)
print(f"The grade for {mark} is: {grade}")

#c

#handle invalid input(non-numeric value)
def grade_students(mark):
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            return 'Invalid Input'
        if mark >=90:
            return 'A'
        elif mark >=80:
            return 'B'
        elif mark >=70:
            return 'C'
        elif mark >=60:
            return 'D'
        else:
            return 'F'
    except ValueError:
        return 'InvalidInput'
    
#Test the function with a valid mark and invalid input
valid_mark = 85
grade = grade_students(valid_mark)
print(f"The grade for valid mark {valid_mark} is: {grade} ")

invalid_input = 'abc'
grade = grade_students(invalid_input)
print(f"The grade for invalid_input is: {grade} ")


#d

def grade_students(mark):
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            return 'Invalid Input'
        if mark >=90:
            return 'A', 'Excellent'
        elif mark >=80:
            return 'B', 'Excellent'
        elif mark >=70:
            return 'C', 'Good'
        elif mark >=60:
            return 'D', 'Satisfactory'
        else:
            return 'F', 'Needs Improvement'
    except ValueError:
        return 'InvalidInput'
    
#e
    
mark = 78
grade, message = grade_students(mark)
print(f"The grade for {mark} is: {grade} : message= {message}")

# a)Write a python program that prints the following pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# b)Write a recursive function to calculate the factorial of a given number n. Test the function with n = 5. 
# c)Write a python program that takes two parameters (a and b) and returns their sum .Test the function with values a = 3 and b=4.
# d)Create a class car with attributes : brand and year. Provide a method in the class to display information about the car.
# e) Create an instance of the class and display the information.

#a)
def print_pattern():
    for i in range (1,6):
        print("".join(str(x) for x in range (1 , i + 1)))
print_pattern()

#b)
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function with n = 5
n = 5
result = factorial(n)
print(f"Factorial of {n} is: {result}")

#c)

def add_nums(a,b):
    return a + b
a = 3
b = 4
result = add_nums(a,b)
print(f"The sum of {a} and {b} is: {result}")

#d)

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
        
    def display_info(self):
        print(f"Car brand : {self.brand} , Year : {self.year}")

#Create an instance of the class
my_car = Car('Benz', 2024)

#display car information
my_car.display_info()

#e)

#Create an instance of the class
my_car = Car('Benz', 2024)

#display car information
my_car.display_info()


#a)Define a python class book with attributes title,author,pages.
# Provide a method in the class to display information about the book.
# Create an instance of the class and display the information.
# b)Create a derived class 'Ebook' that inherits the 'Book' class. 
# Add an additional attribute 'format' to the 'Ebook' class .Display the information for an instance of the Ebook class. 
# c)Create a function on the 'Book' class that returns only the book title and its author. 


# Part (a): Book class with attributes title, author, and pages
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def get_title_and_author(self):
        return f"Title: {self.title}, Author: {self.author}"

# Part (b): Derived class Ebook that inherits from Book and adds 'format' attribute
class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Format: {self.format}")

# Part (a): Creating an instance of Book and displaying its information
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
print("Book Information:")
book1.display_info()

# Part (b): Creating an instance of Ebook and displaying its information
ebook1 = Ebook("1984", "George Orwell", 328, "EPUB")
print("\nEbook Information:")
ebook1.display_info()

# Part (c): Creating an instance of Book and getting only the title and author
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
print("\nBook Title and Author:")
title_and_author = book2.get_title_and_author()
print(title_and_author)




