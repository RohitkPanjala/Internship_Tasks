# Problem 18 - Both players are given the same string, s.
# Both players have to make substrings using the letters of the string s.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# Scoring
# A player gets +1 point for each occurrence of the substring in the string s.
# For Example:
# String s = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 points.

# HackerRank Link: 
# https://www.hackerrank.com/challenges/the-minion-game/problem



def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
