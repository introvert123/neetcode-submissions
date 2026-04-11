class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        #we know that every value in people is <= limit
        #if we can sort it and use two pointers 

        maxValue = max(people)
        count = [0]*(maxValue+1)

        for p in people:
            count[p] += 1

        #sorting
        i = 1
        idx = 0
        while i<=maxValue:
            while count[i]:
                people[idx] = i
                count[i] -= 1
                idx += 1
            i += 1

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            rem = limit - people[right]
            boats += 1
            if rem >= people[left]:
                left += 1
            right -= 1

        return boats



        