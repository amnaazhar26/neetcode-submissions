def add_two_numbers() -> int:
    nums_input = input().split(",")
    return sum([int(x) for x in nums_input])

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
