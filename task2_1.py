def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Each value of total is [0,4,13,15,16]
                                    # and each value of num is [4,9,2,1]
    return total

result = tally([4, 9, 2, 1])