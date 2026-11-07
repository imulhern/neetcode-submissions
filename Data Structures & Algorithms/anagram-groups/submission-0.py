class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for w in strs:
            enc = [0] * 26
            for s in w: 
                enc[ord(s) - ord('a')] += 1 
            if tuple(enc) not in word_map:
                word_map[tuple(enc)] = [w]
            else:
                word_map[tuple(enc)].append(w)
        return list(word_map.values())
        