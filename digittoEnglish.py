def reverse(num):
    rev = 0
    while num>0:
        rev = rev * 10 + num % 10
        num = num / 10
    return rev

def rev_add(num):
    check = num == reverse(num)
    step = 0


    if check:
        print "already palindrome"
    else:
        step += 1
        if step > 1000:
            print "max limit reached 1000 iterations"

        else:
            while not check:
                rev = reverse(num)
                num = num + rev
    return num

print rev_add(195)