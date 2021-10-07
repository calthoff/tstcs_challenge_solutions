# not done

def binary_search(a_list, c):
    first = 0
    last = len(a_list) - 1
    char_code = ord(c)
    while last >= first:
        mid = (first + last)//2
        if a_list[mid] == c:
            return True
        else:
            if char_code < ord(a_list[mid]):
                last = mid - 1
            else:
                first = mid + 1

    return False

print(binary_search(['s','e','l','f'], 'f'))
