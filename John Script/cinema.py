
films = {
    "Finding Dory": [3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while true:

    choice = input("What movie would you like to see?: ").strip().title())

    if choice in films:
        age = int(input("How old are you?: ").strip())
        if age >= films[choice][0]:
                  num_seats = films[choice][1]
                  if num_seats >0:
                      print("Enjoy the film!")
                      films[choice][1] = films[choice][1] - 1
                      
                else:
                    print("You are too young to see that film!")
                
                
        else:
            print("We don't have that film....")
