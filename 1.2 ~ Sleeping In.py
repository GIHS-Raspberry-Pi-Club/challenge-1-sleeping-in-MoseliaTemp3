QueryEnd = "\n   > "
Again = "Invalid Input"
print()

#  This messing around with upper and lower cases is done so that the user can enter an upper or
#  lower case answer without being given an error even though the input was correct.
def CustomisedInput(Statement, Inputs):
    #Make all the possible statements in uppercase.
    for index, item in enumerate(Inputs):
        Inputs[index] = item.upper()
    #Create bracketed option menu for inputs.
    Options = " ("
    for i in Inputs:
        Options += str(i) + "/"
    Options = Options[0 : len(Options) - 1] + ")"
    #Ask for input.
    Output = input(Statement + Options + QueryEnd)
    #Continue asking for inputs until the input is one of the options.
    while not Output.upper() in Inputs:
        print(Again + "\n")
        Output = input(Statement + Options + QueryEnd)
    #Return input in uppercase.
    return Output.upper()


def CanISleepInTomorrow(School, Tuesday):
    if School:
        if Tuesday:
            #If tomorrow is school on Wednesday, sleep in a bit.
            print("You can sleep in tomorrow, but only for a short while.")
        else:
            #If tomorrow is school on other days, don't sleep in.
            print("You cannot sleep in tomorrow.")
    else:
        #If there is no school tomorrow (weekend, holiday, etc), sleep in.
        print("You can sleep in as long as you want.")


def GeneralScript():
    #Ask if school is tomorrow and turn the input into True or False
    print()
    School = True if (CustomisedInput("Do you have school tomorrow?", ["Y","N"]) == "Y") else False

    if School:
        #If school is on, ask if tomorrow is Wednesday and turn the input into True or False.
        print()
        Tuesday = True if (CustomisedInput("Is today Tuesday?", ["Y","N"]) == "Y") else False
    else:
        #If there is no school, make {Tuesday} False so as to not mess with the passing to the CanISleepInTomorrow function.
        Tuesday = False

    #Output resuts of input.
    CanISleepInTomorrow(School, Tuesday)

while True:
    #Run script indefinetally unless the user stop it.
    GeneralScript()
    print("\n")
    if CustomisedInput("------------------------------------------------\nRun again?", ["Y","N"]) == "N":
        break
