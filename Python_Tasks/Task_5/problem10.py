# Problem 10 : You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# HackerRank Link:
# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    s2 = ""
    for i in s:
        if i.islower():
            s2+=i.upper()
        else:
            s2+=i.lower()
                
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
