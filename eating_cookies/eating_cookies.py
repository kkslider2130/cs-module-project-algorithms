'''
Input: an integer
Returns: an integer
'''
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


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 2

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
