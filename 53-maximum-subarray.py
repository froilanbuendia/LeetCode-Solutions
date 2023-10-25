class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        curr = 0
        #iterates through the list
        for i in nums:
            #adds element to curr
            curr += i
            #replaces max to be curr if greater
            if max < curr:
                max = curr
            #if curr is negative then makes it 0
            if curr < 0:
                curr = 0
        return max