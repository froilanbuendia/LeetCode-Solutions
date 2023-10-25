class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # creates a set
        hashset = set()

        # loops through nums list
        for i in nums:
            # checks if i already in hashset
            if i in hashset:
                return True
            # adds i to hashset
            hashset.add(i)
        return False
                