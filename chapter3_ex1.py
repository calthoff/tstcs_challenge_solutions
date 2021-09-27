# not done

def binary_search(a_list, c):
    first = 0
    last = len(a_list) - 1
    while len(a_list) > 0:
        mid = (first + last)//2
        if a_list[mid] == c:
            return True
        else:
            if ord(c) < ord(a_list[mid]):
                last = mid - 1
            else:
                first = mid + 1
    return False

binary_search(['s','e','l','f'], 'f')
