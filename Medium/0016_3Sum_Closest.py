# Given an array nums of n integers and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Input an array of numbers and a target sum
        # Output three numbers that has a sum closest to target, single solution assumed

        # Sort the given numbers
        nums.sort()
        # Initialize result
        res = nums[0]+nums[1]+nums[2]
        if res == target:
            return target
        
        for i in range(len(nums)-2):
            # search for reuslt from the current item to the end from both ends
            j, k = i+1, len(nums)-1
            # All the items are checked if l =< r
            while j < k:
                # Sum the three items
                s = nums[i] + nums[j] + nums[k]
                # Return result if there is a target result 
                if s == target:
                    return target
                # Update result with closet
                if abs(s-target)<abs(res-target):
                    res = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
        # Return the result
        return res
