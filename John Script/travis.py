#create list of users

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]


#create logic to say Hello to user and ask them what their name is
while True:
    print("Hi! My name is Travis")
    name=input("What is you're name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
        
    else:
        print("Hmmmmm I don't think i have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around!")




    




