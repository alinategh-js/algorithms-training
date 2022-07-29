# time: O(n^2) | space: O(n)
def three_number_sum(list, target_sum):
    list.sort() # O(nlog(n))
    result = []
    array_length = len(list)
    for i in range(array_length):
        current_number = list[i]
        left_pointer = i + 1
        right_pointer = array_length - 1
        while left_pointer < right_pointer:
            current_sum = current_number + list[left_pointer] + list[right_pointer]
            if current_sum == target_sum:
                result.append([current_number, list[left_pointer], list[right_pointer]])
                left_pointer += 1
            elif current_sum < target_sum:
                left_pointer += 1
            else:
                right_pointer -= 1
    return result

list = [12, 3, 1, 2, -6, 5, -8, 6]
print(three_number_sum(list, 0))