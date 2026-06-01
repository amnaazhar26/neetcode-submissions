from typing import List

def contains_duplicate(words: List[str]) -> bool:
    set_ = set()
    for w in words:
        if w not in set_:
            set_.add(w)
        elif w in set_:
            return True
    return False

        

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
