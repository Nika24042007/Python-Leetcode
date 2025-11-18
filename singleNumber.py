class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dubl = [0]*(max(nums)+1)
        ind = []
        for i in range(len(nums)):
            if dubl[nums[i]] == 0:
                dubl[nums[i]] = i +1
            else:
                ind.append(dubl[nums[i]] -1)
                ind.append(i)
        ind.sort()
        ind.reverse()
        for i in ind:
            nums.pop(i)
        return nums[0]