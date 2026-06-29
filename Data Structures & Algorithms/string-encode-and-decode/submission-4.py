class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s
        return res

        


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            size = ""
            j = i
            while s[j] != ":":
                size += s[j]
                j += 1
            print(size)
            size = int(size)
            i = j + 1
            res.append(s[j + 1:j + 1 + size])
            i = j + 1 + size        
        return res
        

