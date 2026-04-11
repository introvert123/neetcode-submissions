class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        map1 = {}
        map2 = {}

        for val in s1:
            map1[val] = map1.get(val,0) + 1

        start = 0
        right = 0
        while right < len(s2):
            map2[s2[right]] = map2.get(s2[right],0) + 1

            if right - start + 1 == len(s1):
                if map1 == map2:
                    return True
                else:
                    map2[s2[start]] = map2.get(s2[start],0) - 1
                    if map2[s2[start]] == 0:
                        del map2[s2[start]]
                    start = start + 1

            right += 1

        
        return False
