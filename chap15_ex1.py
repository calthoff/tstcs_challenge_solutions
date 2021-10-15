# not finished yet


def checkMinHeap(A):
    # check for all internal nodes that their left child and
    # right child (if present) holds min-heap property or not

    # start with index 0 (the root of the heap)
    for i in range((len(A) - 2) // 2 + 1):
        if A[i] > A[2 * i + 1] or (2 * i + 2 != len(A) and A[i] > A[2 * i + 2]):
            return False

    return True