class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(L,M,R):
            leftArray = nums[L:M+1]
            rightArray = nums[M+1:R+1]

            i = j = 0
            k = L

            while i < len(leftArray) and j < len(rightArray):
                if leftArray[i] <= rightArray[j]:
                    nums[k] = leftArray[i]
                    i += 1
                else:
                    nums[k] = rightArray[j]
                    j += 1
                k += 1
            
            while i < len(leftArray):
                nums[k] = leftArray[i]
                i += 1
                k += 1
            
            while j < len(rightArray):
                nums[k] = rightArray[j]
                j += 1
                k += 1


        def mergeSort(left, right):

            if left == right: #we have reached single element array
                return
            
            mid = (left + right)//2

            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            merge(left, mid, right)

        mergeSort(0, len(nums) - 1)
        return nums
        