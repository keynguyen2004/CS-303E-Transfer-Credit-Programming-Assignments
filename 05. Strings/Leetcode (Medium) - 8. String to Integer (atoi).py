"""
Leetcode Problem #: 8
Leetcode Problem: String to Integer (atoi)
Difficulty: Medium

This is an integer related question and we should be 
careful about negative integers and overflow and underflow.
Whitespaces must be stripped off. Also, there might be leading 
+ or - symbol. For our solution, we will use isdigit() and 
strip() function

"""
class Solution:
    def myAtoi(self, s):
        
        string, sign = '', 1
        res = s.strip( ) 
         
        if res == "" : 
            return 0 
        
        if res[0] == '+' : 
            res = res[1 : ]      
        elif res[0] == '-' : 
            sign = -1
            res = s[1 : ]
            
        for char in res: 
            if char.isdigit() == False : 
                break  
            string += char
        
        if string == '': 
            return 0 
        
        while len(string) > 1 and string[0] == '0' : 
            string = string[1 : ]
     
        if sign == 1 : 
            if int(string) > 2**31 - 1:
                return 2**31 - 1
            else:
                return int(string)
        else : 
            string = -1 * int(string) 
            if string < -2**31:
                return -2**31
            else:     
                return string



# Alternatively, we can perform mathematical operation on the 
# string using res * 10 + int(char)

class Solution:
    def myAtoi(self, str):

        res, sign = 0, 1
        str = str.strip()

        for index, char in enumerate(str):
            if char.isdigit():
                res = res * 10 + int(char)
                if res * sign > 2**31 - 1:
                    return 2**31 - 1
                if res * sign < -2**31:
                    return -2**31
            elif index == 0:
                if char == "-":
                    sign = -1                    
            else:
                break

        return res * sign
        