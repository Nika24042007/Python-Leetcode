class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = list(s)
        for i in letters:
            if s.count(i) == 1:
                return s.find(i)
        return -1