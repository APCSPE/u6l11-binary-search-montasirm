import math

def binary_search(my_list, target):
    lower_idx = 0
    upper_idx = len(my_list) - 1
    comparisons = 0  # track number of comparisons

    while lower_idx <= upper_idx:
        comparisons = comparisons + 1
        
        mid_idx = math.ceil((lower_idx + upper_idx) / 2) # calculate middle index; ceil function rounds up

        # compare target with value at the middle index
        if my_list[mid_idx] > target:
            print("index " + str(mid_idx) + ": value = " + str(my_list[mid_idx]) + " --> too high!")
            lower_idx = mid_idx + 1 # update lower index
        elif my_list[mid_idx] < target:
            print("index " + str(mid_idx) + ": value = " + str(my_list[mid_idx]) + " --> too low!")
            upper_idx = mid_idx - 1 # update upper index
        else:
            print("index " + str(mid_idx) + ": value = " + str(my_list[mid_idx]) + " --> FOUND!")
            print("number of comparisons: " + str(comparisons))
            return True # target is found, early return true
    
    print("target not in list")
    print("number of comparisons: " + str(comparisons))
    return False # loop ended without returning true, so target not in list


# MAIN PROGRAM
num_list = [50, 48, 44, 39, 34, 33, 31, 29, 25, 25, 22, 21, 18, 14, 13, 13, 10, 8, 5, 3, 2, 1]


# write your test code:
print(binary_search(num_list, 323))
print(binary_search(num_list, 97))
print(binary_search(num_list, 14))
print(binary_search(num_list, 1))

