def countdown(i):
    # print(i)
    if i <= 5:
        print(i)
        return i
    else:
        countdown(i - 1)


countdown(10)
print(countdown(10))
