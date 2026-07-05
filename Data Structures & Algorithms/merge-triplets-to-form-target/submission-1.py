class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            if triplet[0] == target[0] and not x:
                x = True
            if triplet[1] == target[1]and not y:
                y = True
            if triplet[2] == target[2]and not z:
                z = True
        
        return True if x and y and z else False