'''
Input: an integer
Returns: an integer
'''
# first solution
seq = []


def cookie_counter(sequence, actions, k):
    global seq
    current = actions
    max_action = 3
    while max_action > 0:
        if max_action+current == k:
            seq.append(f"{sequence}+{max_action}")
        elif max_action+current < k:
            cookie_counter(f"{sequence}+{max_action}", max_action+actions, k)
        max_action -= 1


def eating_cookies(n):
    max_action = 3
    global seq
    while max_action > 0:
        if max_action == n:
            seq.append(str(n))
        elif max_action < n:
            cookie_counter(str(max_action), max_action, n)
        max_action -= 1
    res = len(seq)
    seq = []
    return res

# second solution

# def eating_cookies(n):
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     return eating_cookies(n-1)+eating_cookies(n-2)+eating_cookies(n-3)

# cache solution

# def eating_cookies(n,cache=None)
#     if n < n:
#         return 0
#     elif n==0:
#         return 1
#     elif cache is not None and cache[n] > 0:
#         return cache[n]
#     else:
#         if cache is None:
#             cache =[0 for i in range(n)]
#         cache[n]= eating_cookies(n-1,cache)+eating_cookies(n-2,cache)+eating_cookies(n-3,cache)

#     return cache[n]


print(eating_cookies(30))
# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(
#         f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
