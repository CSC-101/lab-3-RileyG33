def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # The values of new_list are [4] at idx=0, [4,9] at idx=1,
                                        # [4,9,2] at idx=2, and [4,9,2,1] at idx=3
    return new_list                    # The first loop is a for-loop and uses the values in the list.
                                    # This loop is an index-based loop and uses a range of numbers

result = copy([4, 9, 2, 1])