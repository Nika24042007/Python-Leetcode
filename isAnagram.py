class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = set(list(s))
        l = dict()
        for i in letters:
            l[i] = s.count(i)
        letters = set(list(t))
        for i in letters:
            if i in s:
                if l[i] == t.count(i):
                    pass
                else:
                    return False
            else:
                return False
        return True