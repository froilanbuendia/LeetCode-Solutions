class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
    # def alphaNum(self, c):
    #     # ord gets the ascii number
    #     return (ord('A') <= ord(c) <= ord('Z') or
    #     ord('a') <= ord(c) <= ord('z') or
    #     ord('0') <= ord(c) <= ord('9'))
        
            