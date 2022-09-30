class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findMaxCrossSubArray(A, low, mid, high):
            left = 0
            sum = 0
            max_left = 0
            i = mid
            # finds max subarray from mid to low
            for i in range(mid, low - 1, -1):
                sum += A[i]
                if sum > left:
                    left = sum
                    max_left = i
            right = 0
            sum = 0
            max_right = 0
            #finds max subarray from mid to high
            for j in range(mid + 1, high):
                sum += A[j]
                if sum > right:
                    right = sum
                    max_right = j
            #returns max left index, max right index, and sum of the max left and max right indexes
            return (max_left, max_right, left + right)

        def maxSubArrayDivideAndConquerHelper(nums, low, high):
            #end statement when high is low
            if high == low:
                return (low, high, nums[low - 1])
            else:
                m = (low + high) // 2
                left_low, left_high, left_sum  = maxSubArrayDivideAndConquerHelper(nums, low, m)
                right_low, right_high, right_sum = maxSubArrayDivideAndConquerHelper(nums, m + 1, high)
                cross_low, cross_high, cross_sum = findMaxCrossSubArray(nums, low, m, high)
                #checks which sum is the highest out of the left, right, and cross
                if left_sum >= right_sum and left_sum >= cross_sum:
                    return(left_low, left_high, left_sum)
                elif right_sum >= left_sum and right_sum >= cross_sum:
                    return(right_low, right_high, right_sum)
                else:
                    return(cross_low, cross_high, cross_sum)

        #def maxSubArrayDivideAndConquer(nums: list[int]) -> int: 
        #return the element in the first index is length of nums is 1
        if len(nums) == 1:
                return nums[0]
        #uses a helper function to return just the sum and not the max left index and max right index
        _, _, sum = maxSubArrayDivideAndConquerHelper(nums, 0, len(nums))
        if sum == 0 and 0 not in nums:
            return max(nums)
        return sum