class Solution(object):
    def twoSum(self, arr, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(arr)):
            j = 1
            while j < len(nums):
                sum = arr[i] + arr[j]
                j = j + 1
                if sum == target:
                    print arr[i], arr[j]
                    break
            j = j + 1
if __name__ == '__main___':
    nums  = [2, 7, 11, 15]
    target = 9,
    Solution.twoSum(nums, target)