class Solution:
    def getMinDistance(self, nums, target, start):
        if nums[start] == target:
            return 0
        back, forth = start - 1, start + 1
        if start == len(nums)-1:
            forth = start
        if start == 0:
            back = start
        while back>=0 and forth<len(nums):
            if nums[back] == target:
                return abs(back-start)
            elif nums[forth] == target:
                return abs(forth-start)
            elif back>0:
                back -=1
            elif forth<len(nums)-1:
                forth += 1

s = Solution
a = s.getMinDistance(self=s, nums=[2202,9326,1034,4180,1932,8118,7365,7738,6220,3440], target=3440, start=0)
print(a)