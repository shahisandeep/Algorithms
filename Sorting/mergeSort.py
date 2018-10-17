
def merge_sort(alist):
    if len(alist) <= 1: return alist

    mid = len(alist)/2

    left = merge_sort(alist[:mid])
    print left
    right = merge_sort(alist[mid:])
    print right

    return merge(left, right)

def merge(a, b):
    arr = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            arr.append(a[a_idx])
            a_idx += 1
        else:
            arr.append(b[b_idx])
            b_idx += 1

    if b_idx < len(b): arr.extend(b[b_idx:])
    if a_idx < len(a): arr.extend(a[a_idx:])
    return arr


alist = [2,9,3,5,10,8,14,12]

print merge_sort(alist)


