class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            num = nums[i+1:]
            for j in range(len(num)):
                if nums[i] == num[j]:
                    if abs(i - (i+j+1)) <= k:
                        return True
        return False