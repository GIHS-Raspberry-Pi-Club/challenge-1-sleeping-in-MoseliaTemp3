#Repeatedly used things defined here for ease of modification.
EndBool = "\n  (Y/N) > "
Again = "Incorrect input."

#Begin Program.
while True:
    print("\n")
    
    #Is tomorrow a school day?
    SchoolTomorrow = input("Do you have school tomorrow?" + EndBool)
    print()
    #Repeat question until answer is "y" or "n".
    while not (SchoolTomorrow.lower() == "y" or SchoolTomorrow.lower() == "n"):
        print(Again)
        SchoolTomorrow = input("Do you have school tomorrow?" + EndBool)
        print()
        
    #If tomorrow is a school day, is it a Wednesday?
    if SchoolTomorrow.lower() == "y":
        TomorrowWednesday = input("Is today Tuesday?" + EndBool)
        print()
        #Repeat question until answer is "y" or "n".
        while not (TomorrowWednesday.lower() == "y" or TomorrowWednesday.lower() == "n"):
            print(Again)
            TomorrowWednesday = input("Is today Tuesday?" + EndBool)
            print()

    if SchoolTomorrow.lower() == "n":
        #If there is no school.
        print("You do not have school tomorrow, so you can sleep in as long as you want.")
    elif TomorrowWednesday.lower() == "y":
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
