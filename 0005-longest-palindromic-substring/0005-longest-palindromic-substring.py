class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start from the middle and expand outwards
        if len(s) == 1:
            return s[0]
        elif len(s) == 2:
            if s[0] == s[1]:
                return s[0] + s[1]
            else:
                return s[0]
        res = ''
        s_idx = 0 # start index
        res_l = 0
        for i in range(len(s)): # goes through the string
            # odd length
            l = i
            r = i
            # checks if left and right index are equal and in bounds
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1) > res_l:
                    s_idx = l
                    res_l = r - l + 1
                # decrements and increments left and right
                l -= 1
                r += 1
            # even length
            l = i
            r = i + 1
            # checks if left and right index are equal and in bounds
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1) > res_l:
                    s_idx = l
                    res_l = r - l + 1
                # decrements and increments left and right
                l -= 1
                r += 1
        # creates the string to return
        res = s[s_idx:s_idx + res_l]
        return res