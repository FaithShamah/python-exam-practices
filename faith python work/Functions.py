#FUNCTIONS
#Perform a task(methods)
#def functionName():
#Parameters:Information passed into a function to perform a particular task(Variables that we pass in) eg radius(r)
#Arguments:The values eg radius(r)r=4
#Function calls:A function can't perform a specific task without being called
                 #They are called according to the way they are written
                 #Make sure u r on the same line of def
                 #functionName(3)
                 
#Examples
#1.Create a function that returns the main components of a function.The function shld say main components are:


def function_basics():
    print(f"The main components of a function are body,parameter and arguments.")
function_basics()

#2.Create a function that returns your student name,reg num,and student age.Define variables for student name,reg num,and student age.

def student_details():
    student_name = "Namono Faith"  #local variables
    registration_number = "2024/DSC/0060/SS"    #local variables
    student_age = "21"   #local variables
    print(f"Im {student_name} with registration number {registration_number} and my age is {student_age}")
student_details()

#3.Create a function that returns your student name,reg num,and age as parameters.


def student_data_parameters(name,age,reg_num):  #parameters
    print(f"{name} , {age} , {reg_num}")    #parameters
student_data_parameters('Namono Faith', 21 ,'2024/DSC/0060/SS')   #parameters

##.RETURN VALUES(instead of print we use return)
def my_name_approach_2():
    name = "Faith"
    return name
my_name_approach_2()


#or
# def my_name_parameter_3():
#     name = 'Namono Faith'
#     return name
# my_name_parameter_3('Namono Faith')

def my_age():
    age = "21"
    return age
print(f"My name is {my_name_approach_2()} and im {my_age()}")

#Create a function that calculates the area of a triangle,the base and the height must be function parameters
def area_of_a_triangle(base,height):
    area = int(1/2*base*height)  #if answer should be integer
    print(f"The area of a triangle with base {base} and height {height} is area {area}")
area_of_a_triangle(4,6)
    
#If user should enter height and base
def area_of_a_triangle_approach_2():
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    area = int(1/2*base*height)
    print(f"The area of a triangle with base {base} and height {height} is area {area}")
area_of_a_triangle_approach_2()

