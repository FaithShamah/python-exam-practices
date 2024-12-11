 #Lists & Tuples
#Are mutable /can be changed-items in a list can be changed
#Tuples aren't mutable,items in a tuple can't be changed
#Lists use []/angle brackets
#Tuples use()
#Both are ordered
#Both are indexed

#Examples
#Create both variables for the list and the tuple
#List[]
products = ['pen','pencil','book']
#Tuple()
colors = ('red','green','pink')
#Add rubber to the products list
products.append('rubber')
print(products)
#Insert ruler in the second postion
products.insert(1,'ruler')
print(products)
#Display the length of the list
print(f"The length of the products is:",len(products))
#Add purple to the tupple of colors #First convert to a list and add items,then convert to a tupple
new_colors = list(colors)
print(type(new_colors)) #Converting the tuple to a list
print(new_colors)
new_colors.append('purple')
print(new_colors)
colors = tuple(new_colors) #Converting the list to the tupple
print(type(colors))
print(colors)

#Tuple with one item
fruits = ('apple')
print(fruits,type(fruits)) #Stating the type of the variable # on a single tuple you use a comma
