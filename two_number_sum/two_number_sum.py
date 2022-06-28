def two_number_sum_1(array, target_sum): # Time: O(n^2) | Space: O(1)
    array_length = len(array)
    for i in range(array_length - 1):
        first_number = array[i]
        for j in range(i+1, array_length):
            second_number = array[j]
            if first_number + second_number == target_sum:
                return (first_number, second_number)
    return ()

def two_number_sum_2(array, target_sum): # Time: O(n) | Space: O(n)
    dic = {}
    for i in range(len(array)):
        current_number = array[i]
        target_number = target_sum - current_number
        if dic.get(target_number):
            return (current_number, target_number)
        else:
            dic[current_number] = True
    return ()

def two_number_sum_3(list, target_sum): # Time: O(nlogn) | Space: O(1)
    # first we need to sort our algorithm
    # because in this problem our focus is not on implementing a sorting algorithm,
    # we can use python's built-in sort which uses Timsort which runs at O(nlogn) in time
    list.sort()
    list_length = len(list)
    left_pointer = 0
    right_pointer = list_length-1
    while left_pointer < right_pointer:
        sum = list[left_pointer] + list[right_pointer]
        if sum == target_sum:
            return (list[left_pointer], list[right_pointer])
        elif sum > target_sum:
            right_pointer -= 1
        else:
            left_pointer += 1
    return ()

# let's use array instead of list for better performance
list = [3, 5, -4, 8, 11, 1, -1, 6]
result = two_number_sum_3(list, 10)
print(result)