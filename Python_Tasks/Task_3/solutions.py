# Q1. Find the Frequency of Each Word in a Sentence
# Write a Python program to count how many times each word appears in a given sentence and store the result in a dictionary.
# Example Input:
# python is easy and python is powerful
# Expected Output:
# {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

def wrd_freq(s):
    s2 = s.split()
    wrd_d = {}

    for i in s2:
        if i in wrd_d:
            wrd_d[i]+=1
        else:
            wrd_d[i]=1

    return wrd_d        


# 2. Frequency of each character

def freq_ch(w):

    ch_d = {}
    for i in w:
        if i in ch_d:
            ch_d[i]+=1
        else:
            ch_d[i]=1

    return ch_d        

# 3. Non Repeating Character

def non_rep(w):
    n_dic = {}
  #  lst = []
    x = " "
    for i in w:
        if i in n_dic:
            n_dic[i]+=1
        else:
            n_dic[i]=1

    for k,v in n_dic.items():
        if v == 1:
            x = k        
            break

    return x

# 4. Strings Anagram        

def st_agrm(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()


    if len(s1)!=len(s2):
        return False

    for ch in s1:
        c1 = 0
        c2 = 0

        for i in s1:
            if i == ch:
                c1+=1

        for i in s2:
            if i == ch:
                c2+=1

        if c1!=c2:
            return False                
    return True

# 5. First Repeating Character in String

def first_repeat(s):
    char_f = {}
    x = " "

    for i in s:
        if i in char_f:
            char_f[i]+=1
        else:
            char_f[i]=1

    for k,v in char_f.items():
        if v > 1:
            x = k
            break

    return k            

# 6. Move All Zeros to the End of a List

def mv_zeros(nums):
    lst = []

    for i in nums:
        if i!=0:
            lst.append(i)

    z = len(nums) - len(lst)

    for i in range(1,z+1):
        lst.append(0)            

    return lst    



# 7. Find the Second Highest Distinct Number in a List

def sec_dist(lst):
    lst2 = []

    for i in lst:
        if i not in lst2:
            lst2.append(i)

    high_num = lst2[0]
    sec_num = lst2[0]

    for i in lst2:
        if i > high_num:
            sec_num = high_num
            high_num =i
        elif i > sec_num and i!=high_num:
            sec_num = i

    return sec_num

# 8. Remove Duplicates Without Changing the Original Order

def rem_dup(lst):
    lst2 = []

    for i in lst:
        if i not in lst2:
            lst2.append(i)

    return lst2                        

# 9. Find the Missing Number from 1 to N

def miss_num(nums):

    n = len(nums)

    e_sum = n * (n+1) // 2
    a_sum = sum(nums)

    m_num = a_sum - e_sum

    return m_num

# 10. 

def sum_pair(nums,tar):
    lst = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == tar:
                # print(nums[i],nums[j])
                lst.append(nums[i])
                lst.append(nums[j])
    return lst            

# 11. Find the Number Closest to Zero

def close_zero(lst):
    closest = lst[0]

    for i in lst:
        if abs(i) < abs(closest):
            closest = i
        elif abs(i) == abs(closest) and i > closest:
            closest = i

    return closest

# 12. Find Common Elements Between Two Lists

def com_lsts(lst1,lst2):
    lst3 = []

    for i in lst1:
        if i in lst2:
            lst3.append(i)

    return lst3                

# 13. 


def rotate_right(nums, k):
    n = len(nums)
    k = k % n

    result = []

    for i in range(n - k, n):
        result.append(nums[i])

    for i in range(0, n - k):
        result.append(nums[i])

    return result

# 14. 

def con_sum(lst):
    max_sum = lst[0] + lst[1]

    for i in range(1,len(lst)-1):
        curr_sum = lst[i] + lst[i+1]

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum        

# 15. 


def sum_target(nums, target):
    pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                a = nums[i]
                b = nums[j]

                if a > b:
                    a, b = b, a

                pair = [a, b]

                if pair not in pairs:
                    pairs.append(pair)

    pairs.sort()
    return pairs











