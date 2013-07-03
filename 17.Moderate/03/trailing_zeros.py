def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def trailing_zeros(n):
    total = fact(n)
    zeros = 0
    while total % 10 == 0:
        zeros = zeros + 1
        total = total / 10
    return zeros


def trailing_zeros_smart(n):
    zeros = 0
    for i in xrange(1, n + 1):
        num = i
        while num % 5 == 0:
            zeros = zeros + 1
            num = num / 5
    return zeros


print trailing_zeros(4)
print trailing_zeros_smart(4)
print trailing_zeros(6)
print trailing_zeros_smart(6)
print trailing_zeros(10)
print trailing_zeros_smart(10)
print trailing_zeros(100)
print trailing_zeros_smart(100)
print trailing_zeros(998)  # Can't do more than 998 with this function
print trailing_zeros_smart(998)
print trailing_zeros_smart(99999)
