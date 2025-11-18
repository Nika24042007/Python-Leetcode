class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i+1:]
            for j in range(len(num)):
                if num[j] + nums[i] == target:
                    return [i, j+i+1]