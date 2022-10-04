# Author: Eden Will Sng Jin Xuan
# Admin No: 201520M
# this is part 2 of the vending machine assignment
# ----------
# Declaring List
# ----------
#
inv = {  # creates inventory of vending Machine
        'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
        'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 20},
        'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 40},
        'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 0},
        '1P': {'description': '100 Plus', 'price': 1.1, 'quantity': 50},
        'CC': {'description': 'Coca cola', 'price': 1.3, 'quantity': 50}

    }


#
# ----------
# Declaring functions
# ----------
#


def isFloat(prompt, errorMsg):  # function which check whether user input is a float
    notFloat = True  # a while loop that loops until return input
    while notFloat is True:
        try:  # tries until user put a valid input
            theinput = float(input(prompt))  # user inputs the prompt checks if its a float
            if theinput > 0:    # checks whether if value is positive
                round(theinput, 1)  # round off the number due to float being 1 decimal place
                return theinput  # returns back the value
            else:
                print("Please input a positive number")  # inform user that they have put a negative number
        except:  # if input is not a float
            print(errorMsg)  # inform user that input they have entered is not a float


def isInt(prompt, errorMsg):  # check whether user input is a integer
    notInt = True  # a while loop that loops until return input
    while notInt is True:
        try:    # tries until user put a valid input
            theinput = int(input(prompt))  # user inputs the prompt checks if integer
            if theinput >= 0:   # checks whether if value is positive
                return theinput  # ends the loop and returns the input
            else:
                print("Please input a positive number")   # inform user that they have inputted a negative number
        except:
            print(errorMsg)  # inform user that input they have entered is not a float


def isEmpty(prompt, errorMsg):  # check whether user input blank
    empty = True  # a while loops until return input
    while empty is True:
        theinput = input(prompt)  # prompts user to input
        if theinput == "" or theinput == " " or theinput.isspace() is True:  # validates if user input empty
            print(errorMsg)  # tells user that their input is empty
        elif len(theinput) > 20:  # checks if the description is less than 20 characters
            print("Please input less than 20 characters")  # prompts user to input less than 20 characters
        else:
            return theinput  # returns back a value


def isValidId(prompt, errorMsg, inventory):  # ensures drink id is only 2-4 characters long
    isNotValid = True
    while isNotValid is True:
        theinput = input(prompt)  # prompts user to input a drink Id
        if 1 < len(theinput) < 5:  # checks if the id is within 2-4 characters
            if theinput.upper() in inventory:  # checks if the input is already in the inventory
                print("Drink id exist!")     # tells user that their input is already in the inventory
                continue  # repeats the loop
            else:
                return theinput.upper()  # returns drink id
        else:
            print(errorMsg)  # error msg telling user that they did not input the correct format


def displayDrink(inventory):  # a function which displays the drink
    newList = []   # creates a list
    newList2 = []
    for p in inventory:  # iterates over description and price length to find the longest string
        length = (len(inventory[p]['description']))  # check length of description
        newList.append(length)  # appends to list
        priceLength = round(len(str(inventory[p]['price'])), 1)  # check length of price
        newList2.append(priceLength)  # appends to list
    for q in inventory:  # iterates the description of the product
        description = inventory[q]['description']  # variable to put description
        price = (inventory[q]['price'])   # variable to put price of inventory
        priceRounded = ' (S$%.1f)' % price   # variable to put rounded off pricing
        qty = inventory[q]['quantity']   # a variable to hold the quantity
        if qty <= 0:     # checks whether the quantity in dictionary is 0
            theQty = "  ***out of stock***"  # if 0 change to out of stock
        else:
            theQty = '  Qty : ' + str(qty)   # else show the qty
        iterate = q + '. ' + description.ljust(max(newList)) + priceRounded.ljust((max(newList2) + 4)) + theQty  # this will print out a sentence of the dictionary key
        print(iterate)  # prints the full dictionary in a nice orderly fashion


def add_drink_type(drink_id, description, price, quantity):  # drink id function
    inv[drink_id] = {'description': description, 'price': price, 'quantity': quantity}  # adds new drink


def replenish_drink(drink_id, quantity):  # function to replenish drink
    inv[drink_id]['quantity'] += quantity   # changes quantity


def addDrinkProcess(prompt, errorMsg, inventory):   # a function which goes through the process of adding a new drink
    isNotInside = True
    while isNotInside is True:  # while loop to keep attempting until user gets it right
        theinput = input(prompt)   # prompts user to input
        if theinput.upper() in inventory:   # checks dictionary if inv item quantity is greater than 5
            if inventory[theinput.upper()]['quantity'] > 5:
                print("No need to replenish. Quantity is greater than 5.")
            else:
                return theinput.upper()   # returns the drink which needs to be replenished

        else:
            print(errorMsg)   # error msg to tell user that they have inputted something wrong


def chooseDrink(prompt, errorMsg, inventory):   # function that ask user to pick a drink
    notDrinkId = True
    while notDrinkId is True:   # while loop to ensure user gets it right
        theinput = input(prompt)
        if theinput.upper() in inventory:  # check if the input is in inventory (therefore valid option)
            return theinput.upper()  # capitalised it so it works
        elif theinput == "0":  # allows user to input 0 , to cancel their purchase
            return theinput
        else:  # error msg for invalid inputs
            print(errorMsg)

#
#  ----------
#  End of functions
#  ----------
#


loop = True
while loop is True:
    cart = []   # shopping cart
    uChoice = ""  # variable that requires user to input their choices
    isavendor = input("Are you a vendor (Y/N)? ")  # inputs whether user is a vendor
    # N means user using is not a vendor, prompt them to choose a product
    #
    # ----------
    #  Part 1
    # ----------
    #
    if isavendor.upper() == "N":  # validation whether user chose not a vendor, if not a vendor given the option of these drinks
        displayDrink(inv)  # shows drink
        print("0. Exit / Payment")
        payment = 0  # declaring variable that will be  payment of drinks
        totalChoice = 0  # counter to count number of drinks
        #
        # while loop to loop infinitely until 0
        while uChoice != "0":  # as long as user does not implement 0, it will loop
            uChoice = chooseDrink("Enter Choice:", "Error in choice, please enter a choice", inv)  # if user inputs 0, loop will be broken and the machine will restart
            if uChoice == "0":
                break  # 0 will end the loop, because user did not choose any product
            else:
                if inv[uChoice]['quantity'] == 0:
                    print(inv[uChoice]['description'], 'is out of stock')  # tells user that item picked is out of stock
                else:
                    payment += inv[uChoice]['price']  # adds to the total payment needed
                    totalChoice += 1   # tells user the total amount of choices
                    inv[uChoice]['quantity'] -= 1  # deducts the quantity in real time
                    cart.append(uChoice)   # keeps track of drink in cart
                    print("no. of drinks selected = ", totalChoice)
        if totalChoice == 0:  # validation checks that checks whether if no drink choices is made the vending machine will restart
            print("No drinks was chosen, Good Bye")
            continue  # stop all processes and go back to the top " Are you a vendor? "
        notPaid = True
        while notPaid is True:  # a loop that runs as long as user would like to pay
            print("Please pay: $%.2f" % payment, "\nIndicate your payment:")  # announces to user what they are required to pay
            tenNote = isInt("Enter no. of $10 notes: ", "Please input a number")  # prompts user to input the number of $10 notes they have
            totalCash = 0  # a variable which will reset if user doesnt not have sufficient cash
            totalCash = totalCash + 10*tenNote  # tabulates the total  cash user has inputted
            #
            if totalCash >= payment:  # checks whether total cash is more than payment
                notPaid = False   # this would end the loop once the instructions for this loop has finished
            else:
                fiveNote = isInt("Enter no. of $5 notes: ", "Please input a number")   # prompts user to input the number of $5 notes they have
                totalCash = totalCash + 5*fiveNote  # tabulates the total  cash user has inputted, carries over from the previous 10$ input if the amount deposited is insufficient
            #
            if totalCash >= payment:  # checks whether total cash is more than payment
                notPaid = False  # this would end the loop once the instructions for this loop has finished
            else:
                twoNote = isInt("Enter no. of $2 notes: ", "Please input a number")  # prompts user to input the number of $2 notes they have
                totalCash = totalCash + 2*twoNote  # tabulates the total  cash user has inputted, carries over from the previous input if the amount deposited is insufficient
            #
            if totalCash >= payment:  # checks whether total cash is more than payment
                notPaid = False  # this would end the loop once the instructions for this loop has finished
            else:
                print("Not enough to pay for the drinks \nTake back your cash! ")  # if not enough, this will inform user that they did not deposit sufficient cash
                confirmCancel = True  # new variable for while loop
                while confirmCancel is True:  # loops as long as user did not put Yes (Y) or No (N)
                    buyAgain = input("Do you want to cancel the purchase? Y/N: ")  # ask if want cancel purchase
                    if buyAgain.upper() == "N":  # user does not cancel purchase
                        confirmCancel = False   # ends the loop once all functions are completed
                    elif buyAgain.upper() == "Y":  # user cancel purchase
                        print("Purchase is cancelled. Thank you.")
                        confirmCancel = False  # ends the loop once all functions are completed
                        notPaid = False  # ends the payment loop
                        for i in cart:   # basically the return process, returns back items which user did not buy
                            inv[i]['quantity'] += 1  # a for loop to add back all items to vending machine
                    else:
                        print("invalid input, please input Y or N ")  # ensures user put either Yes or No
                continue  # returns back to payment while loop
            change = totalCash - payment   # calculates user changes
            print("Please collect your change: $%.2f" % change, "\nDrinks paid. Thank you. \n")  # informs user the change they will receive and then tells user good bye

            break  # resets the machine
    # Y means user using is a vendor prompt user to choose a option
    #
    # ----------
    #  Part 2
    # ----------
    #
    elif isavendor.upper() == "Y":  # user input Y means they're the vendor
        print("Welcome to ABC Vending Machine.")  # welcome message
        while uChoice != "0":
            print("Select from following choices to continue:")  # prompts user to pick a choice
            print("1.  Add Drink Type")
            print("2.  Replenish Drink")
            print("0.  Exit")
            uChoice = input("Enter Choice:")  # if user inputs 0, loop will be broken and the machine will restart
            if uChoice == "0":
                break
            elif uChoice == "1":  # begins the process of adding a new drink
                drinkId = isValidId("Enter drink id: ", "Please enter only 2-4 characters", inv)  # activates the function, rationale for 2-4 characters is because drink ID should not be too long
                desc = isEmpty("Enter description of drink (20 Characters Limit): ", "Please enter a description (20 Characters Limit")
                # rationale for character limit is because a vending machine has a finite number of pixels it can display ,
                #  if user inputs too much for the description of drink
                cost = isFloat("Enter price: $", "Please Input a number")  # gathers the price for the drink, includes validation
                amt = isInt("Enter quantity: ", "Please Input a number")  # gathers the quantity of drinks, includes validation
                # quantity can be 0 because the person adding new drink may not be the supplier who as the drink at hand currently, therefore we accept 0
                add_drink_type(drinkId, desc, cost, amt)  # adds drink to dictionary
                print(desc, " added!")  # informs user that their drink is added
                continue  # ends the loop
            elif uChoice == "2":  # begins process of replenishing a drink
                displayDrink(inv)  # activates display drink list
                drinkId = addDrinkProcess("Enter drink id: ", "No drink with this drink id. Try again.", inv)  # ask user to add drink, validates if drink exists
                amt = isInt("Enter Quantity: ", "Please input a number")  # ask user for drink quantity validates if user inputs a number
                replenish_drink(drinkId, amt)   # function which adds drink
                topUp = inv[drinkId]['description']  # variable to hold what user has top up
                print(topUp, "has been top up!")  # tells user the drink top up is completed
                continue
            else:
                print("Invalid option")  # validation check
    else:  # for false errors
        print("invalid input please input Y or N \n\n")  # if user did not enter a proper value
        continue  # reset vending machine
