class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}

        for i, num in enumerate(nums):
            pair = target - num

            if pair in num_dict:
                return [i, num_dict[pair]]
            
            num_dict[num] = i
        