#!/bin/python3

def find_smallest_positive(xs):
    if not xs:
        return None

    def search(left, right):
        if left == right:
            if xs[left] > 0:
                return left
            else:
                return None
        mid = (left + right) // 2
        if xs[mid] > 0:
            right = mid
        if xs[mid] < 0:
            left = mid + 1
        if xs[mid] == 0:
            return mid + 1
            left = mid + 1
        return search(left, right)
    return search(0, len(xs) - 1)


def count_repeats(xs, x):
    if not xs:
        return 0

    def find_first_occ(left, right, x):

        #if the only thing in arr is x, return left. Otherwise return None
        if left == right:
            if xs[left] == x:
                return left
            else:
                return None
        # initialize result = None
        result = None

        # find the middle value
        mid = (left + right) // 2

        # if the target is located, update the result and
        # search towards the left (lower indices)
        if x == xs[mid]:
            result = mid
            if mid != 0 and xs[mid - 1] == x:
                right = mid - 1
            else:
                return result

        # if the target is less than the middle element, discard the left half
        elif x < xs[mid]:
            left = mid + 1

        # if the target is more than the middle element, discard the right half
        else:
            right = mid - 1
        return find_first_occ(left, right, x)
    first_index = find_first_occ(0, len(xs) - 1, x)

    def find_last_occ(left, right, x):

        # if the only thing in arr is x, return left. Otherwise return None
        if left == right:
            if xs[left] == x:
                return left
            else:
                return None
        # initialize result = None
        result = None

        # find the middle value
        mid = (left + right) // 2

        # if the target is located, update the result and
        # search towards the upper (right indices)
        if x == xs[mid]:
            result = mid
            if mid + 1 < len(xs) and xs[mid + 1] == x:
                left = mid + 1
            else:
                return result

        # if the target is less than the middle element, discard the left half
        elif x < xs[mid]:
            left = mid + 1

        # if the target is more than the middle element, discard the right half
        else:
            right = mid - 1
        return find_last_occ(left, right, x)
    last_index = find_last_occ(0, len(xs) - 1, x)
    print("first_index=", first_index)
    print("last_index=", last_index)
    if last_index is not None and first_index is not None:
        return (last_index - first_index) + 1
    else:
        return 0


def argmin(f, lo, hi, epsilon=1e-3):
    if hi - lo < epsilon:
        return (hi + lo) / 2
    m1 = lo + (hi - lo) / 3
    m2 = hi - (hi - lo) / 3
    if f(m1) < f(m2):
        return argmin(f, lo, m2, epsilon)
    else:
        return argmin(f, m1, hi, epsilon)

##########################################################################
# the functions below are extra credit
##########################################################################


def find_boundaries(f):
    pass


def argmin_simple(f, epsilon=1e-3):
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
