class Solution(object):
    def removeDuplicates(self, nums):
        idx = 0

        for i in range(1, len(nums)):
            if nums[idx] != nums[i]:
                idx += 1
                nums[idx] = nums[i]
                
        return idx + 1