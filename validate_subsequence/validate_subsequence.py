""" 
subsequence (subarray) of a given sequence (array) is any sequence that
can be derived from the given sequence by deleting some or no elements 
without changing the order of the remaining elements
"""
# Time complexity: O(n)
# Worst case scenario occurs when we traverse through the whole array
def validateSubsequence(array, subsequence):
    subsequence_index = 0
    subsequence_length = len(subsequence)
    array_length = len(array)
    for i in range(0, array_length):
        if array[i] == subsequence[subsequence_index]:
            subsequence_index += 1
        if subsequence_index == subsequence_length:
            return True
    return False

array = [1, 5, 10, -1, -5, 23, 42, 89, -120]
subsequence1 = [5, -1, 23, -120]
subsequence2 = [1, -1, 23, 42]
subsequence3 = [1, -1, 10, 42]
print(validateSubsequence(array, subsequence1))
print(validateSubsequence(array, subsequence2))
print(validateSubsequence(array, subsequence3))