class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = 0
        post = 0
        
        for i in nums:
            pre += i
            
        for i in range(len(nums[::-1])):
            pre -= nums[i]
            if pre == post:
                return i
            post += nums[i]
        return -1