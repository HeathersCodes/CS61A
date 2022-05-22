def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    num, mod = x // 10, x % 10
    while num > 0:
        print(num, num%10)
        if num % 10 > mod:
            return False
        mod = num % 10
        num //= 10    
    return True
print(ordered_digits(21))
