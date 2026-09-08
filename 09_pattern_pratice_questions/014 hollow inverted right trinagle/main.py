"""
Problem Description:

You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', where the first row contains n stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be left-aligned.



Input:

A single integer n, where 1 <= n <= 100.



Output:

A list of strings where each string represents a row in the hollow inverted right-angled triangle.



Example:

Input: 4
Output: ['****', '* *', '**', '*']

Input: 5
Output: ['*****', '*  *', '* *', '**', '*']
"""

def generate_hollow_inverted_right_angled_triangle(n):
    triangle = []
    
    for i in range(n, 0, -1):
        if i == n or i == 1:
            triangle.append('*'*i)
        elif i < n and i > 1:
            triangle.append('*' + ' '*(i-2) + '*')
    
    return triangle