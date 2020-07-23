'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# first pass
# def single_number(nums):
#     singles =[]
#     for num in nums:
#         if num not in singles:
#             singles.append(num)
#         else:
#             singles.remove(num)
#     return singles

# alternative


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

# def single_number(nums):
#     counts={}
#     for num in nums:
#         if num not in counts:
#             counts[num]=1
#         else:
#             counts[num]+=1
#     for k,v in counts.items():
#         if v == 1:
#             return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
