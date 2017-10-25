#Repeatedly used things defined here for ease of modification.
EndBool = "\n  (Y/N) > "
Again = "Incorrect input."

#Begin Program.
while True:
    print("\n")
    
    #Is tomorrow a school day?
    Query1 = input("Do you have school tomorrow?" + EndBool)
    print()
    #Repeat question until answer is "y" or "n".
    while not (Query1.lower() == "y" or Query1.lower() == "n"):
        print(Again)
        Query1 = input("Do you have school tomorrow?" + EndBool)
        print()
        
    #If tomorrow is a school day, is it a Wednesday?
    if Query1.lower() == "y":
        Query2 = input("Is today Tuesday?" + EndBool)
        print()
        #Repeat question until answer is "y" or "n".
        while not (Query2.lower() == "y" or Query2.lower() == "n"):
            print(Again)
            Query2 = input("Is today Tuesday?" + EndBool)
            print()

    if Query1.lower() == "n":
        #If there is no school.
        print("You do not have school tomorrow, so you can sleep in as long as you want.")
    elif Query2.lower() == "y":
        #If there is school, but its a late Wednesday.
        print("You have school tomorrow, but it is a Wednesday so you can sleep in a bit.")
    else:
        #If there is school and it is not a late Wednesday.
        print("You have school tomorrow and cannot sleep in.")

    #Repeat program or break loop?
    print()
    if input("Run again?" + EndBool).lower() != "y":
        print()
        break
