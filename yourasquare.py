def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    sqrt = n ** 0.5
    print(sqrt.is_integer())
    return sqrt.is_integer()

is_square(64)