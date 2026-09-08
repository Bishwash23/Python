"""
Problem Description:

You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a list of strings. Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.



Input:

A single integer n, where 1 <= n <= 100.



Output:

A list of strings where each string represents a row in Floyd's Triangle.



Example:

Input: 5
Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']

Input: 3
Output: ['1', '2 3', '4 5 6']
"""

def generate_floyds_triangle(n):
    triangle = []
    
    num = 1
    for i in range(1, n+1):
        row = ' '.join(str(num + j) for j in range(i))
        triangle.append(row)
        num += i
    return triangle