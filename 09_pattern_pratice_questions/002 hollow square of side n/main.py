"""
You are given an integer n. Your task is to return a hollow square pattern of size n x n made up 
of the character '*', represented as a list of strings. The hollow square has '*' on the border, 
and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input: 3
Output: ['***', '* *', '***']

Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']
"""

def generate_hollow_square(n):
    square = []
    
    if n == 1:
        square.append('*')
        return square
    
    square.append('*'*n)
    
    for i in range(n-2):
        square.append('*' + ' '*(n-2)+ '*')
    
    square.append ('*'*n)
    
    return square