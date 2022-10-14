class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_l = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1) > res_l:
                    res = s[l:r + 1]
                    res_l = len(res)
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1) > res_l:
                    res = s[l:r + 1]
                    res_l = len(res)
                l -= 1
                r += 1
        return res