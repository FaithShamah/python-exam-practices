#Sum
#Find the sum of 6 and 5 and print the result
#sum 
#Given that we have 2 products a laptop and a mouse such that the price of a laptop is 300,000 and the price of a mouse is 50,000,use a for loop to find the total sum of the products.
laptop = [300000]
mouse = [50000]
sum = 0
product_prices =[300000,50000]
for price in product_prices:
    sum+=price
print(f"The total sum of the products is: {sum:,}")

bag = [50000]
pen = [500]
book = [5000]
sum = 0
product_prices =[50000,500,5000]
for price in product_prices:
    sum+=price
print(f"The total sum of the items is: {sum:,}")

