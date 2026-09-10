#Code challenge 3
#Global Freight Calculator

name = input("Sender Name: ")
item = input("Type of item: ")
is_Fragile = input("is it fragile? ")
if is_Fragile == "True":
	print("We will treat it with care")
weight = float(input("Weight in kg: "))
distance = float(input("Distance in km: "))
is_express = input("express? True or False: ") == "True"
is_international = input("Is it international? True or False: ") == "True"
base_cost = (weight * 2.50) + (distance * 0.15)


#Free Shipping
if weight <= 2 and distance <= 100 and not is_express and not is_international:
	print("It will be Free Shipping")

#International Express
elif is_express and is_international:
	price = (base_cost * 1.40) + 50
	print("International Express price $",price)

#Express or Heavy International
elif is_express or (is_international and weight > 20):
	price = (base_cost * 1.20) + 25
	print("Express or Heavy International fee is $",price)

#Oversized
elif weight > 30 or distance > 1000:
	price = base_cost + 30
	print("Oversized fee is $",price)

#Standard rate
else:
	print("The base price is $",base_cost)
