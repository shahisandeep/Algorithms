# get the reversed number
def reverse_num(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

# check if the number is a palindrome
def is_palindrome(n):
    rev_num = reverse_num(n)
    return n == rev_num

def reverse_add(num):
   count = 0

   if is_palindrome(num):
       return num
   else:
    while not is_palindrome(num):
       count = count + 1
       rev = reverse_num(num)
       num = num + rev

   return count, num


print reverse_add(input())