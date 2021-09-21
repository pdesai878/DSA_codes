def bisect_left(a, x):
    '''returns i where all a[:i] is less than x'''
    lo, hi = 0,len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < x: lo = mid + 1
        else: hi = mid
    return lo

def bisect_right(a, x):
    '''returns i where all a[:i] is less than or equal to x'''
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] > x: hi = mid
        else: lo = mid + 1
    return lo

arr=[2,3,3,4,7,9]
print(bisect_left(arr,3))
print(bisect_right(arr,3))
