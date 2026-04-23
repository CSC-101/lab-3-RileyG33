def check(n:int) -> bool:
    return n > 2                             # The values of n are [0,1,2,3,4].
                                             # The corresponding return values are
                                            # False, False, False, True, True


answer = [x for x in range(5) if check(x)]   # The value of answer is [3,4]
print()