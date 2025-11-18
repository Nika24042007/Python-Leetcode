class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in nums2:
            nums1.append(i)
        ind = []
        for i in range(n+m):
            if nums1[i] == 0:
                ind.append(i)
        ind.reverse()
        for i in ind:
            nums1.pop(i)
        nums1.sort()
