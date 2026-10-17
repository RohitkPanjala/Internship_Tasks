# Problem 17: You have a record of $n$ students containing their names and percentage scores in Math, Physics, and Chemistry. Given a student's name, output their average percentage correct to 2 decimal places.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
students = {}

for i in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    students[name] = marks

    query_name = input()

    avg = sum(students[query_name]) / len(students[query_name])

    print(f"{avg:.2f}")