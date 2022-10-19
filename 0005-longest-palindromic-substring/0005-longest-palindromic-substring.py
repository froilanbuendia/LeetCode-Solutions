class Solution:
    def longestPalindrome(self, s: str) -> str:
        #start from the middle and expand outwards
        #check for both odd and even bounds
        res = ''
        s_idx = 0
        res_l = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1) > res_l:
                    s_idx = l
                    res_l = r - l + 1
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1) > res_l:
                    s_idx = l
                    res_l = r - l + 1
                l -= 1
                r += 1
        res = s[s_idx:s_idx + res_l]
        return res

