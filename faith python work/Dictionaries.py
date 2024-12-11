
#Dictionaries
#A key value pair
#Syntax,access,change,add,remove,loop thru
#Clear is another function in a dictionary
student = {'name':'Gillian','age':22,'location':'Muyenga'}
print(student)
fruits = {1:'Apple',
          2:'Orange',
          3:'Banana'
          }
print(fruits)

#WHENEVER they tell you to access the items in a dictionarry it means you access the values
#We use the keys to access values / items in a dictionary
#Access the name,age and location
print(student['name'])
print(student['age'])
print(student['location'])

#Print the keys of the student dictionary.
print(student.keys())

#Print the length of the dictionary
print(f"The length of the dictionary is:",len(student))

#Add a key contact to the student dictionary
student["contact"]='0750767890'
print(student)

#Update the name Gillian to Apio Gillian
student["name"]='Apio Gillian'
print(student)

#Access/Print all the values the dictionary
print(student.values())

#Remove the contact key from the dictionary
student.pop('contact')
print(student)