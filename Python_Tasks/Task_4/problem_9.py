# Problem 9: Read a given string, change the character at a given index with a specified character, and print the modified string.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/python-mutations/problem

def mut_str(s,p,k):
    l = list(s)

    l[p] = k

    s =''.join(l)

    return s

s = input()
i, c = input().split()
s_new = mut_str(s, int(i), c)
print(s_new)