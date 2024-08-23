from isPalindrome import isPalindrome

run = True

while run:
    # initial message for user; takes input and converts to lowercase
    item = (input("Enter a string to check for palindrome. Q to quit: ").lower())
    # if item is not equal to the char q then the program keeps running
    if item != "q":
        # initializes the class isPalindrome for future use
        IP = isPalindrome()

        # uses the print_statement from the isPalindrome class to check for palindrome
        palindrome_check = IP.print_statement(item)

        # prints the return statement for the user
        print(palindrome_check)

    else:
        # if "q" is entered in the input, the program prints Goodbye 
        # and sets run equal to false to terminate
        print("Goodbye.")
        run = False
