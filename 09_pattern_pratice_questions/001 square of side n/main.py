"""
    001 Square of side 'N'
    Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.
"""

def generate_square(n):
    square = []
    
    for i in range(n):
        square.append(n*'*')
    
    return square