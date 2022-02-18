# Write a code that prints out the first occurrence of a duplicate in a given array of integers
#     Sample Input: [1,2,3,2,1]
#     Output: 2

# Solution :
# By checking the count of every element from the input list.
# If the count is greater than 1 then thaT element is the first duplicate in the list.


def get_first_repeating_element(input):
    for i in range(len(input)):
        if input.count(input[i]) > 1:
            return input[i]
    return "Not Found!"


input = [4, 2, 3, 1, 1, 4]
print(get_first_repeating_element(input))
