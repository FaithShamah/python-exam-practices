name = "Birungi"
for item in name:
    print(item)
    
marks = [60,70,80]
for mark in marks:
    print(mark)
    
def total_marks():
    marks = [60,70,80]
    sum = 0
    for mark in marks:
        sum+=mark
        print(f"The total mark is: {sum}")
total_marks()

#RANGE FUNCTION
#We must lnow the syntax for range function,it works with the parameters start,stop,step.
#Basic Example
#Priny all numbers from 0 to 6
#Hint:Use a range function
#o-6(0,1,2,3,4,5,6) #0 is the start,6 is the stop
for number in range (7):
    print(number)
    
#Write a simple program that prints numbers btn 0 to 10
for num in range (11):
    print(num)
 
#Print numbers btn 1 to 20
def one_to_twenty():
    for numb in range (1,21): # start is 1,stop is 20
        print(numb)
one_to_twenty()

#Print the following range of even numbers from (2,4,6,8,10)
def even_numbers():
    for even_numbers in range (2,11,2): #the start is 2,stop is 11,step is 2,if you dont pass in a step,it will be 0,if you pass in 1,it will be one,and 0,it will be an error.
        print(even_numbers)
even_numbers()

#Print the following range of odd numbers from (0,3,5,7,9)  
def odd_numbers():
    for odd_numbers in range (1,10,2):
        print(odd_numbers)
odd_numbers()
    
 