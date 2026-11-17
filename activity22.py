anime_type = ["isekai","adventure", "scifi","romance"]
anime_title = [ ]

while True:
    ans = input("Do you know any anime? Yes or No?")

    if ans.lower( ) == 'yes' :
        print ("what is its type? select from the list ")
        for x in anime_type:
            print(x)
        a_type = input("type: ")

        title = input("what is the title of the anime? ")
        anime_title.append(title)
        continue
    else:
        print("Thank you")
        break