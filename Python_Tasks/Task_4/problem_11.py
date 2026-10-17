# Problem 11: Given a string $s$, check if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase characters, and uppercase characters. Print True or False for each across 5 separate lines.
# HackerRank Link: 
# hhttps://www.hackerrank.com/challenges/string-validators/problem



s = input()
    
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))                