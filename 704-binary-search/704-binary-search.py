class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        for i in nums:
            if i == target:
                return index
            index += 1
        return -1
        