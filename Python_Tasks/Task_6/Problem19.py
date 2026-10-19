# Problem 19 - Company Logo

# HackerRank Link -
# https://www.hackerrank.com/challenges/most-commons/problem

if __name__ == '__main__':
    s = input()
    
    d = {}
    
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
                
for k, v in sorted(d.items(), key=lambda item:(-item[1], item[0]))[:3]:
    print(f"{k} {v}")
