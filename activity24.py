animals = ["Cat", "Fish", "Bird", "Frog", "Snake"]

#dictionary
#key, value
animals_d = {"Walk":"Cat", "Swim":"Fish", "Fly":"Bird", "Jump":"Frog", "Slither":"Snake" }

print(animals[4])


#Traversing dictionary
for x, y in animals_d.items():
    print("key is ",x," value is ",y)
