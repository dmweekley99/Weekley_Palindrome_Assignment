class isPalindrome:
    def palindrome_check(str, start_length, end_length):
        '''Recursive function that takes the parameters of the string, starting position of the str(start_length)
        and ending position of the string(end_length) to determine if the string given is a palindrome and returns True or False'''
        
        if start_length == end_length: # if start and end length are the same, the string is a palindrome
            return True
        
        if str[start_length] != str[end_length]: # compares the start length to the end length of a string 
            return False # returns false if the character is not the same
        
        if start_length < end_length + 1: # cycles through the function as long as the start length is less than the end length
            return isPalindrome.palindrome_check(str, start_length + 1, end_length - 1) # increases the start length and decrease the end length
        
        return True # returns true when the start length is greater than the end length
    
    def initialize_pal(self, str):
        '''This function initializes the string to be checked by determining the ending length of the string
        and calling the palindrome check function as long as the string is not 1 character long'''
        sl = 0 # beginning position
        el = len(str) - 1 # length of string minus 1 to get the overall end position

        if sl == el: # determines if the starting length and ending length are the same
            return True
        
        else: # uses palindrome_check with the string, starting length, and ending length initialized
            return isPalindrome.palindrome_check(str, sl, el)
    
    def print_statement(self, text):
        '''returns a statement to tell the user if the string the entered is a palindrome'''
        b = self.initialize_pal(text) # initializes the string to check if it is a palindrome
        if b == True: # if initialize_pal is True then it is a palindrome
            return f'{text} is a palindrome.'
        else: # if not True it is not a palindrome
            return f'{text} is not a palindrome.'
