from solutions import wrd_freq
from solutions import freq_ch
from solutions import non_rep
from solutions import st_agrm
from solutions import first_repeat
from solutions import sec_dist
from solutions import rem_dup
from solutions import miss_num
from solutions import mv_zeros
from solutions import sum_pair
from solutions import close_zero
from solutions import com_lsts
from solutions import rotate_right
from solutions import con_sum
from solutions import sum_target
# 1. Word Frequency

frq = wrd_freq("python is easy and python is powerful")
print(frq)

# 2. Char Frequency

c_freq = freq_ch("banana")
print(c_freq)

# 3. Non-Repeating 
no_rep = non_rep("swiss")
print(no_rep)

#4. String Anagram

s_anagram = st_agrm("silent","listen")
print(s_anagram)

# 5. First Repeating Character in String

f_wrd = first_repeat("programming")
print(f_wrd)

# 6.

z_mv = mv_zeros([0, 3, 0, 1, 2, 0, 4])
print(z_mv)

# 7.
sec_val = sec_dist([10, 20, 40, 30, 40, 20])
print(sec_val)

# 8.
r_dup = rem_dup([4, 2, 4, 5, 2, 7, 5])
print(r_dup) 

# 9. 

m = miss_num([1, 2, 4, 5, 6])
print(m)

# 10.

l = [2, 7, 11, 15]
k = 9
s_pair = sum_pair(l,k)
print(s_pair)

# 11. 

l = [-8, -3, 2, 5, -2]
c_zero = close_zero(l)
print(c_zero)

# 12.

lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
c_lsts = com_lsts(lst1,lst2)
print(c_lsts)

# 13. 

nums = [1, 2, 3, 4, 5]
k = 2

print(rotate_right(nums, k))

# 14. 

l = [4, 7, 2, 9, 5]
print(con_sum(l))


# 15.

nums = [2, 4, 3, 5, 7, 8, 1]
target = 9

print(sum_target(nums, target))