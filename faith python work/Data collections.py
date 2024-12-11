#DATA COLLECTIONS
#These are also data types but the difference is that they store different/multiple items.
#EG:Lists-CRUD definition,sytax(create,read,update,delete),Sets,Tupples,Dictionaries
#1.Lists
varName = [] #This is the syntax we follow
studentNames =["Sandra" , "Patricia" , "Phionah" , "Anitah" ]
studentMarks =["80" , "56" , "78" , "90"]
data = ["Faith" , 90 , " Kamwokya"] #mixed items

#Access the whole list
print(studentNames, type(studentNames))

#Accessing list items
#Indexes(Positive indexing)
print(studentNames[0]) #first item
print(studentNames[1]) #second item
print(studentNames[2]) #third item
print(studentNames[3]) #last item

#Indexes(Negative indexing)
print(studentNames[-4]) #first item
print(studentNames[-3]) #second item
print(studentNames[-2]) #third item
print(studentNames[-1]) #last item

#Appending means adding new items to a list
#At the End
studentNames.append("Michelle")
print(studentNames)

#At a particular position
studentNames.insert(2,"Peace")
print(studentNames)