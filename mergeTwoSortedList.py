def merge(a = [], b = []):
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






a = [3,4, 7, 10]
b = [1,5,9]

print merge(a, b)
#[1, 3, 4, 5, 7, 9]