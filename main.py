from isPalindrome import isPalindrome

ip = isPalindrome()
run = True
while run:
    text = input("Enter a string to check for palindrome. Q to quit: ").lower()
    if text == "q":
        print("Goodbye")
        run = False 
    else:
        result = ip.print_statement(text)
        print(result)

