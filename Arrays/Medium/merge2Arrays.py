class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_num1, index_num2 = m-1,n-1
        merge_index = m + n - 1
        print(merge_index)
        while index_num2 >= 0:
            if index_num1 >= 0 and nums1[index_num1] > nums2[index_num2]:
                nums1[merge_index] = nums1[index_num1]
                index_num1 -= 1
            else:
                nums1[merge_index] = nums2[index_num2]
                index_num2 -= 1
            merge_index -= 1
        return nums1
        