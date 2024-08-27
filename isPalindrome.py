class isPalindrome:
    def palindrome_check(str, start_length, end_length):
        if start_length == end_length:
            return True
        
        if str[start_length] != str[end_length]:
            return False
        
        if start_length < end_length + 1:
            return isPalindrome.palindrome_check(str, start_length + 1, end_length - 1)
        
        return True
    
    def initialize_pal(self, str):
        sl = 0
        el = len(str) - 1 

        if sl == el:
            return True
        
        else:
            return isPalindrome.palindrome_check(str, sl, el)
    
    def print_statement(self, text):
        b = self.initialize_pal(text)
        if b == True:
            return f'{text} is a palindrome.'
        else:
            return f'{text} is not a palindrome.'
