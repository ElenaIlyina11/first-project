def digit_root(num):
    if num <= 9:
        return num
    else:
        result = 0
        for i in str(num):
            result += int(i)
        return digit_root(result)


print(digit_root(97569))
