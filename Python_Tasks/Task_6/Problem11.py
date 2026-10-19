# Problem 11 - 
# Given an integer, n, print the following values for each integer i from 1 to n:
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

# HackerRank Link - 
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1,number+1):
        dec = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        print(dec.rjust(width), octal.rjust(width),
              hexa.rjust(width), binary.rjust(width))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
