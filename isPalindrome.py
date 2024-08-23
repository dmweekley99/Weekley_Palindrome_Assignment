class isPalindrome():
    def __init__(self):
        '''initializes stack and reverse input string used later'''
        self.stack = []
        self.reverse = ""
    
    def push(self, char):
        '''adds character to stack'''
        self.stack.append(char)
    
    def pop(self):
        '''removes character from stack and adds to string in reverse order'''
        while self.stack:
            # while there is a stack, removes the last character from stack
            character = self.stack.pop()
             # last character is added to string 
             # and string is returned when stack is None
            self.reverse += character
        return self.reverse
    
    def split_char(self, input):
        '''uses push function to add each individual 
        character from input from stack'''
        for char in input:
            self.push(char)

    def palindrome_determination(self, input):
        '''function determines if input is the same 
        as the reverse and returns boolean value'''
        item = input
        self.split_char(item)
        backwards = self.pop()
        if input == backwards:
            return True
        else:
            return False
    
    def print_statement(self, input):
        '''function returns user friendly message based 
        on whether or not the input is a palindrome'''
        boolean = self.palindrome_determination(input)
        if boolean == True:
            return f'{input} is a palindrome.'
        else: 
            return f'{input} is not a palindrome.'
            