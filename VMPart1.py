# Author: Eden Will Sng Jin Xuan
# Admin No: 201520M
# This is part 1 of the vending machine assignment
# ----------
# Declaring Function
# ----------
#
def isInt(prompt, errorMsg):  # check whether user input is a integer
    notInt = True
    while notInt is True:
        try:
            theinput = int(input(prompt))
            if theinput >= 0:
                return theinput
        except:
            print(errorMsg)
#
# ----------
# End Of Function
# ----------
#


loop = True
while loop:
    isavendor = input("Are you a vendor (Y/N)? ")  # inputs whether user is a vendor
    print("Welcome to ABC Vending Machine.")  # welcome message
    print("Select from following choices to continue:")  # prompts user to pick a choice
    # N means user using is not a vendor, prompt them to choose a product
    if isavendor.upper() == "N":  # validation whether user chose not a vendor, if not a vendor given the option of these drinks
        print("IM. Iced Milo (S$1.5)")
        print("HM. Hot Milo (S$1.2)")
        print("IC. Iced Coffee (S$1.5)")
        print("HC. Hot Coffee (S$1.2)")
        print("1P. 100 Plus (S$1.1")
        print("CC. Coca Cola (S$1.3)")
        print("0. Exit / Payment")
        payment = 0  # declaring variable that will be  payment of drinks / resets the total payment of drinks
        totalChoice = 0  # counter to count number of drinks  / counter to count number of drinks
        uChoice = ""  # variable that requires user to input their choices
        # while loop to loop infinitely until 0
        while uChoice != "0":  # as long as user does not implement 0, it will loop
            uChoice = input("Enter Choice:")  # if user inputs 0, loop will be broken and the machine will restart
            if uChoice == "0":
                break
            elif uChoice.upper() == "IM":  # if user inputs Ice Milo
                payment += 1.5    # a counter to add up  the payments
                totalChoice += 1  # a counter to add up total choices given
            elif uChoice.upper() == "HM":   # if user inputs Hot Milo
                payment += 1.2
                totalChoice += 1
            elif uChoice.upper() == "IC":  # if user inputs Ice Coffee
                payment += 1.5
                totalChoice += 1
            elif uChoice.upper() == "HC":  # if user inputs Hot Coffee
                payment += 1.2
                totalChoice += 1
            elif uChoice.upper() == "1P":  # if user inputs 100 Plus
                payment += 1.1
                totalChoice += 1
            elif uChoice.upper() == "CC":  # if user inputs Coca Cola
                payment += 1.3
                totalChoice += 1
            else:
                print("Invalid option")  # validation check
                continue
            print("no. of drinks selected = ", totalChoice)  # tells user number of drinks selected after choosing a drink
        if totalChoice == 0:  # validation checks that checks whether if no drink choices is made the vending machine will restart
            print("No drinks was chosen, good bye")
            continue  # stop all processes and go back to the top " Are you a vendor? "
        notPaid = True
        while notPaid is True:  # a loop that ensures user pays
            print("Please pay: $%.2f" % payment, "\nIndicate your payment:")  # ask user to indicate their payment
            tenNote = isInt("Enter no. of $10 notes: ", "Please input a number")  # a validation check is conducted to see if user inputs a integer
            totalCash = 0  # a variable to hold the total number of cash
            totalCash = totalCash + 10*tenNote  # calculates total number of ten dollar notes plus the existing amount of cash
            if totalCash >= payment:   # check if the total cash is more than or equal to the payment
                notPaid = False  # if notPaid = false it stops the loop, thus skipping all if else statement since they're all the same
            else:
                fiveNote = isInt("Enter no. of $5 notes: ", "Please input a number")  # else statement ask user if they have five dollar notes
                totalCash = totalCash + 5*fiveNote  # tabulates total number of  $2 notes + previous amount deposited if any
            if totalCash >= payment:  # check if the total cash is more than or equal to the payment
                notPaid = False   # if notPaid = false it stops the loop, thus skipping all if else statement since theyre all the same
            else:
                twoNote = isInt("Enter no. of $2 notes: ", "Please input a number")  # else statement ask user if they have two dollar notes
                totalCash = totalCash + 2*twoNote  # tabulates total number of  $2 notes + previous amount deposited if any
            if totalCash >= payment:  # final check if the total cash given if more or equals to the payment
                notPaid = False
            else:
                print("Not enough to pay for the drinks\n Take back your cash! ")  # tells user that the user gave insufficient cash
                confirmCancel = True  # a new loop variable
                while confirmCancel is True:  # loops until conditions met
                    buyAgain = input("Do you want to cancel the purchase? Y/N: ")  # ask user if they wish to cancel purchase
                    if buyAgain.upper() == "N":  # user doesnt want to cancel purchase
                        confirmCancel = False  # tells this loop to end, jumps to continue which will reloop the payment process
                    elif buyAgain.upper() == "Y":  # user wants to cancel purchase
                        print("Purchase is cancelled. Thank you.")  # tells user purchase is cancelled
                        confirmCancel = False  # tells loop to end
                        notPaid = False  # tells parent loop(the payment process) to end
                    else:
                        print("invalid input. Please input Y or N")  # tells user to input Y or N
                continue  # returns back to payment while loop
            change = totalCash - payment  # calculate the change for the user
            print("Please collect your change: $%.2f" % change, "\nDrinks paid. Thank you. ")  # tells user their change and goodbye
            break  # resets the machine back to "Are you a Vendor?"
    # Y means user using is a vendor prompt user to choose a option
    elif isavendor.upper() == "Y":
        print("1.  Add Drink Type")
        print("2.  Replenish Drink")
        print("0.  Exit")
        print("\n")
    # for false errors
    else:
        print("invalid input please try again")
