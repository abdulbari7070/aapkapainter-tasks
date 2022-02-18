#  Write a code that checks if two given strings are anagrams
#     Sample Input: Mary Army
#     Output: Yes


# Solution1:
# In this solution we can simply sort the list and compare them 
# If the comparision matches then both the strings are anagrams


def check_and_print_anagrams1(str1, str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        print("Yes")
    else:
        print("No")


# Solution2:
# In this solution we can get the ascii value of each character and sum it 
# If the total value matches for both the string then it is anagrams 

def check_and_print_anagrams2(str1, str2):
    total1 = 0
    total2 = 0
    for char in str1:
        total1 += ord(char)
    for char in str2:
        total2 += ord(char)
    if total1 == total2:
        print("Yes")
    else:
        print("No")


input_str1 = "read"
input_str2 = "dear"


check_and_print_anagrams1(input_str1, input_str2)
check_and_print_anagrams2(input_str1, input_str2)