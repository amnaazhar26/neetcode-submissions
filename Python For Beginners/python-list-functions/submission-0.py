from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum_ = 0
    for n in nums:
        sum_ += n
    return sum_

def get_min(nums: List[int]) -> int:
    min_ = nums[0]
    for n in nums:
        if n <= min_:
            min_ = n
        else:
            continue
    return min_

def get_max(nums: List[int]) -> int:
    max_ = nums[0]
    for n in nums:
        if n >= max_:
            max_ = n
        else:
            continue
    return max_

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
