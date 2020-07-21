'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    i = 0
    j = i+1
    while j < len(arr):
        if j == i:
            j += 1
        elif arr[j] == arr[i]:
            i += 1
            j = 0
        else:
            j += 1
    return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
