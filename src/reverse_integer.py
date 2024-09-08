def reverse_integer(x):
    if x == 0:
        return 0
    
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0
    
    while x != 0:
        pop = x % 10 # extracts the rightmost digit of x using the modulo operator
        x //= 10 # removes the rightmost digit from x by performing integer division by 10
        reversed_x = reversed_x * 10 + pop
        
        # This checks if the reversed integer exceeds the 32-bit signed integer range ([-2^31, 2^31 - 1]). If it does, the function returns 0.
        if reversed_x > 2**31 - 1 or reversed_x < -2**31:
            return 0
    
    return sign * reversed_x


def test_reverse_integer():
    x = 123
    assert reverse_integer(x) == 321

    x = -123
    assert reverse_integer(x) == -321

    x = 120
    assert reverse_integer(x) == 21