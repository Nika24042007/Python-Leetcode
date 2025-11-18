class Solution:
    def isHappy(self, n: int) -> bool:
        sn = list(str(n))
        while len(sn) > 1:
            res = 0
            for i in sn:
                res += int(i)**2
            if res == 1:
                return True
            sn = list(str(res))
        return False