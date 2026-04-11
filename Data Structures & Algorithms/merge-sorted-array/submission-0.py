class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        len1 = len(nums1)
        len2 = len(nums2)

        i = j = 0
        k = 0

        left = nums1[0:m+1]
        right = nums2[0:n+1]

        while i < m and j < n:
            if left[i] < right[j]:
                nums1[k] = left[i]
                i += 1
            else:
                nums1[k] = right[j]
                j += 1
            k += 1
        
        while i < m:
            nums1[k] = left[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = right[j]
            j += 1
            k += 1
        