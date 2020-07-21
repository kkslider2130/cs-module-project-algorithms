'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    start = 0
    end = start+k
    largest = -999999
    new_arr = []
    while end <= len(nums):
        for i in nums[start:end]:
            if i >= largest:
                largest = i
        new_arr.append(largest)
        largest = -999999
        start += 1
        end += 1
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
