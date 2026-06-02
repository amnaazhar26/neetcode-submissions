from typing import List

def read_integers() -> List[int]:
    str_list = input().split(",")
    for i in range(len(str_list)):
        str_list[i]=int(str_list[i])
    return str_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
