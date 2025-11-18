def removeDuplicates(self, nums: List[int]) -> int:
        num = []
        d =[]
        for i in range(len(nums)):
            if nums[i] in d:
                num.append(i)
            else:
                d.append(nums[i])
        num.reverse()
        for i in num:
            nums.pop(i)
        return len(nums)