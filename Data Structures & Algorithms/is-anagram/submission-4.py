class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for c in s: 
            chars[c] = chars.get(c,0) + 1
        print(chars)
        for c in t:
            if c not in chars:
                return False
            else:
                chars[c] -= 1 
                if chars[c] == 0:
                    chars.pop(c)
        if len(chars) == 0:
            return True
        
        return False