def binary_search(user_list, item):
    low = 0
    high = len(user_list) - 1
    print(high)

    while low <= high:
        mid = (low + high) // 2
        guess = user_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9,11, 13, 15, 17, 19]
print(binary_search(my_list, 5))

# 1.1 log2(128) = 7 checks
# 1.2 +1 check = 8 checks
