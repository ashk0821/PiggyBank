#Aashir Khan
#Unit 2- Electronic Piggy Bank

#I start off the program by welcoming the user, asking for the amount of money already in the piggy bank, and listing the options.
print("Welcome to the Electronic Piggy Bank")
total = float(input("How much money is currently in the piggy bank?"))
coin = input("MENU: \n (p) - Deposit a penny. \n (n) - Deposit a nickel. \n (d) - Deposit a dime. \n (q) - Deposit a quarter. \n (e) - Exit program. ")

#I put in a while loop to keep the program continous and program what is supposed to happen if the uCs.ser chooses penny.
while coin != "e":
    if coin == "p":
        total+= 0.01
        print("New balance: %.2f" % total)
        coin = input("Choose a letter to insert another coin.")
#I use a few "elif" statements to continue the loop. 
    elif coin == "n":
        total+= 0.05
        print("New balance: %.2f" % total)
        coin = input("Choose a letter to insert another coin.")
    elif coin == "d":
        total+= 0.1
        print("New balance: %.2f" % total)
        coin = input("Choose a letter to insert another coin.")
    elif coin == "q":
        total+= 0.25
        print("New balance: %.2f" % total)
        coin = input("Choose a letter to insert another coin.")
#Finally, I program what is supposed to happen if the user chooses any other key that isn't p, n, d, q, or e.
    else:
        print("Invalid option")
        coin = input("Choose a letter to insert another coin.")

#Once the user chooses e, the program says "Goodbye!" and finishes the program.
print("Goodbye!")
print("\t Press enter to exit.")
