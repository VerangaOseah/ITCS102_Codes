#Code challenge 3
#Global Freight Calculator

name = input("Sender Name: ")
item = input("Type of item: ")
is_Fragile = bool(input("is it fragile"))
if is_Fragile == True:
	print("We will treat it with care")
else:
	print("Thank you")
weight = int(input("Weight: "))
distance = int(input("Distance: "))
is_express = bool(input("express? "))
is_international = bool(input("Is it international? "))

