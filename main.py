from isPalindrome import isPalindrome

ip = isPalindrome() # initializes class isPalindrome for future use
run = True 
while run: # allows the program to cycle through until the user inputs "q"
    text = input("Enter a string to check for palindrome. Q to quit: ").lower() # takes the users input and converts it to lower case
    if text == "q": # if "q" is entered by the user the program terminates
        print("Goodbye")
        run = False 
    else: # all other strings will use the print_statement function to determine if the string is a palindrome
        result = ip.print_statement(text)
        print(result)

