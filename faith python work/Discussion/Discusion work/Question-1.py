# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 
         #Soln
def temperature_classifier(temp):
    if temp < 0:
        return "Freezing"
    elif 0 <= temp <=10:
        return "Cold"
    elif 11 <= temp <= 20:
        return "Moderate"
    elif 21 <= temp <= 30:
        return "Warm"
    else: 
        return "Hot"
try:
    temperature = float(input("Enter the temperature in °C: "))
    classification = temperature_classifier(temperature)
    print(f"The temperature is classified as: {classification}")
except ValueError:
    print("Please enter a valid number")
    
    
# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**3. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place
      #Soln
import math
def calculate_volume_of_the_sphere(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume
radius = float(input("Enter the radius of the sphere: "))
volume = calculate_volume_of_the_sphere(radius)
print(f"The volume of the sphere with radius{radius} is {volume:.1f}")
    
# Question 2(i)
# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 


def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

# Example usage:
weight = 70  # in kilograms
height = 1.75  # in meters
bmi, category = calculate_bmi(weight, height)
print(f"BMI: {bmi:.2f}, Category: {category}")

         
         
# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)


import math

def calculate_cylinder_volume(radius, height):
    """Calculate the volume of a cylinder given its radius and height."""
    volume = math.pi * (radius ** 2) * height
    return volume

# Example usage:
r = 5  # radius
h = 10  # height
volume = calculate_cylinder_volume(r, h)
print(f"The volume of the cylinder is: {volume:.2f}")


#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail 


def get_grade(score):
    """Function to determine the grade based on score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 50 <= score < 60:
        return 'E'
    else:
        return 'Fail'

def display_grades(scores):
    """Function to display grades for a list of scores."""
    for score in scores:
        grade = get_grade(score)
        print(f'Score: {score} - Grade: {grade}')

def main():
    """Main function to run the grading system."""
    # List of student scores
    student_scores = [95, 82, 76, 65, 54, 45, 88, 92, 71, 40]
    
    print("Student Grades:")
    display_grades(student_scores)

if __name__ == "__main__":
    main()


#Question 4(i)
#Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.


# Initial list of favorite foods
favorite_foods = ["Pizza", "Sushi", "Ice Cream", "Tacos", "Pasta"]

# Adding two more items to the list
favorite_foods.append("Burgers")
favorite_foods.append("Salad")

# Removing one item from the list
favorite_foods.remove("Tacos")

# Printing the updated list
print("Updated list of favorite foods:")
print(favorite_foods)



#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.


# Given list of numbers
numbers = [2, 5, 8, 10, 3, 6]

# Print the first and last elements of the list
first_element = numbers[0]
last_element = numbers[-1]
print("First element:", first_element)
print("Last element:", last_element)

# Print the list in reverse order
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

# Calculate and print the sum of all the elements in the list
sum_of_elements = sum(numbers)
print("Sum of all elements:", sum_of_elements)
