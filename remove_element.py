class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = []
        for i in range(len(nums)):
            if nums[i] == val:
                ind.append(i)
        ind.reverse()
        for i in ind:
            nums.pop(i)
        return len(nums)