def square(n:int) -> int:
    return n * n                           # The values of n are [1, 2, 3, 4]
                                           # The corresponding return values are [1, 4, 9, 16]


squares = [square(x) for x in [1,2,3,4]]   # The value of squares is [1,4,9,16] This relates to the
print()                                    # values recorded above because they are the same