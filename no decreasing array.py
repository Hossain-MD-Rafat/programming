class Solution:
    def checkPossibility(nums):
        count = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count += 1
                if i>0 and i < len(nums) - 2 and (nums[i+1]<nums[i-1]) and (nums[i] > nums[i + 2]):
                    count += 1
                if count>=2:
                    return 0
        return 1

s = Solution
print(s.checkPossibility([3,4,2,3]))