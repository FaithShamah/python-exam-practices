#OOP's(Object Oriented Programming)
#An object is also an instance,it is found in a class
#Here we create objects that do not exist and we give them classes,objects
#Modeling-Trying to identify classes and attributes in each class
#The things that we want the class to do are the methods

#Examples
#1.Creating classes 
#Classes names always start with a capital letter and it's always singular.
#Syntax class Name:
##class Cohort:
    #name
    #description
    #start_date
    #end_date
    #total_number_of_students
    #All the objects are strings.
    
#Within the cohort class:
#Add a constructor for the cohort class.hint read about constructors
#Add a method(function to the class that prints the cohort name and the total number of student
#Create a new instance(object) of the cohort class.hint newCohort = Cohort()
class Cohort:
    def __init__(self, name, description, start_date, end_date, cohort_name, total_number_of_students):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.cohort_name = cohort_name
        self.total_number_of_students = total_number_of_students
        
    def __str__(self):
        return(f"{self.name}, {self.description}, {self.start_date}, {self.end_date}, {self.cohort_name} , {self.total_number_of_students}")

p1 = Cohort(f"Namono Faith", "Programming In Python", "20/August/2024", "20/August/2026",  "Cohort Four" , 56)
print(p1)

newCohort = Cohort(
    name="Mbabazi Hafiswa",
    description="Law",
    start_date="20/August/2025",
    end_date="20/August/2027",
    cohort_name="Cohort Five",
    total_number_of_students="70"
)

print(f"Name: {newCohort.name}")
print(f"Description: {newCohort.description}")
print(f"Start date: {newCohort.start_date}")
print(f"End date: {newCohort.end_date}")
print(f"Cohort name: {newCohort.cohort_name}")
print(f"Total number of students: {newCohort.total_number_of_students}")
