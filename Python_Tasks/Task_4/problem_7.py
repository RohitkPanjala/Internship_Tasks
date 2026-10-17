# Problem 7: You are given a string. Split the string on a " " (space) delimiter and join it using a - hyphen.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem





def sp_jn(s):
    s = s.split()

    s = "-".join(s)

    return s

    


st = "Hello World"
x = sp_jn(st)
print(x)