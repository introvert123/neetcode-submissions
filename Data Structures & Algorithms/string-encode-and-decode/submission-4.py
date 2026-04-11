class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = len(s)
            res = res + str(n) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        string = ""
        newstr = ""
        list1 = []
        length = -1

        i = 0
        while i<len(s):
            if s[i] != '#':
                string = string + s[i]
                i = i + 1
            elif s[i] == '#':
                length = int(string)
                start = i + 1
                end = i + length + 1
                newstr = s[start:end]
                list1.append(newstr)
                i = end
                string = ""

        return list1
