# Problem 12 - You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/capitalize/problem


def solve(s):
    s2 = ""
    words = s.split(" ")

    for i in words:
        if len(i) > 0:
            s2 += i[0].upper() + i[1:]
        s2 += " "

    return s2[:-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
