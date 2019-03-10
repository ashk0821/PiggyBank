#Aashir Khan
#Unit 2- Electronic Piggy Bank

print("Welcome to the Electronic Piggy Bank")
total = float(input("How much money is currently in the piggy bank?"))
coin = input("MENU: \n (p) - Deposit a penny. \n (n) - Deposit a nickel. \n (d) - Deposit a dime. \n (q) - Deposit a quarter. \n (e) - Exit program. ")
#I start off the program by welcoming the user, asking for the amount of money already in the piggy bank, and listing the options.
while coin != "e":
    if coin == "p":
        total+= 0.01
        print("New balance: %.2f" % total)
        coin = input("Choose a letter to insert another coin.")
#I put in a while loop to keep the program continous and program what is supposed to happen if the uCs.ser chooses penny.
    elif coin == "n":
        total+= 0.05
        print("New balance: %.2f" % total)
        coin = input("Choose a letter to insert another coin.")
#I use an "elif" statement to continue the loop. These 4 lines of codes demonstrate what is supposed to happen if user chooses nickel.
    elif coin == "d":
        total+= 0.1
        print("New balance: %.2f" % total)
        coin = input("Choose a letter to insert another coin.")
#I continue with the "elif" statements to demonstrate what happens if the user chooses dime.
    elif coin == "q":
        total+= 0.25
        print("New balance: %.2f" % total)
        coin = input("Choose a letter to insert another coin.")
#The last "elif" statement programs what is supposed to happen if the user chooses quarter.
    else:
        print("Invalid option")
        coin = input("Choose a letter to insert another coin.")
#Finally, I program what is supposed to happen if the user chooses any other key that isn't p, n, d, q, or e.

print("Goodbye!")
print("\t Press enter to exit.")
#Once the user chooses e, the program says "Goodbye!" and finishes the program.