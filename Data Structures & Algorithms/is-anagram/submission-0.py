class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters={}
        t_letters={}
        for letter in s:
            if letter not in s_letters:
                s_letters[letter]=s.count(letter)
        for letter in t:
            if letter not in t_letters:
                t_letters[letter]=t.count(letter)
        if s_letters==t_letters:
            return True
        return False
