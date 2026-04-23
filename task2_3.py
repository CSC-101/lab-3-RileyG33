def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # new_list stars []. Then goes to [5] at value 4, [5,10] at value 9,
                                        # [5,10,3] at value 3 and [5,10,3,2] at value 1
    return new_list

result = increment_all([4, 9, 2, 1])