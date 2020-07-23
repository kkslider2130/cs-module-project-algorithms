'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    i = 0
    length = len(arr)
    while i <= length:
        if arr[i] == 0:
            arr.append(arr.pop(i))
            i -= 1
            length -= 1
        i += 1
    return arr

# initialize left and right
# left is 0
# right is last index in arr
# while left <= right:
# if left points at a zero and right is non-zero
  # swap left and right in original arr
  # inc left
  # dec right
# else
  # if left is non-zero
    # inc left
# if right is zero
    # dec right

# alt:
# def moving(arr):
#     left=0
#     right=len(arr)-1
#     while left <= right:
#         if arr[left]==0 and arr[right]!=0:
#             arr[left],arr[right]=arr[right],arr[left]
#             left+=1
#             right-=1
#         else:
#             if arr[left]!=0:
#                 left+=1
#             if arr[right]=0:
#                 right-=1


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
