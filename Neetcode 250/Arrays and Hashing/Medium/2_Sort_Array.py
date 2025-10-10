#https://leetcode.com/problems/sort-an-array/description/
'''Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''
class Solution:

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        i = 0
        j = 0
        ans = []
        while (i<len(left)) and (j<len(right)):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        while (i<len(left)):
            ans.append(left[i])
            i += 1
        
        while (j<len(right)):
            ans.append(right[j])
            j += 1
        
        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
