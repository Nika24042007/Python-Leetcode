class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num = list(set(nums))
        n = []
        if len(num) > 1:
            num.sort()
            for i in range(len(num)-1):
                if num[i+1]-num[i] != 1:
                    for j in range(num[i+1]-num[i]-1):
                        n.append(num[i]+j+1)
            return n
        else:
            return [num[0]+1]