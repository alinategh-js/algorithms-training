# here a special array is an array that contains integers and/or other special arrays
# so it looks kinda recursive
# time: O(n) | space: O(D)
# important note: n is the total number of all the integers in the array and subarrays
# and d is the maximum depth of subarrays in the array
def calculate_product_sum(special_array: list, depth = 1):
    array_length = len(special_array)
    total_sum = 0
    for i in range(array_length):
        if isinstance(special_array[i], list):
            total_sum += calculate_product_sum(special_array[i], depth + 1)
        else:
            total_sum += special_array[i]
    return total_sum * depth

my_list = [5, 2, [7, -1], 3, [6, [-13, 8] , 4]]
print(calculate_product_sum(my_list))