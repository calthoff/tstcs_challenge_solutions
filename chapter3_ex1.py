def binary_search(a_list, c):
    first = 0
    last = len(a_list) - 1
    target_code = ord(c)
    while last >= first:
        mid = (first + last)//2
        if a_list[mid] == c:
            return True
        else:
            if target_code > ord(a_list[mid]):
                first = mid + 1
            else:
                last = mid - 1

    return False

print(binary_search(['a', 'b', 'c', 'd'], 'b'))


