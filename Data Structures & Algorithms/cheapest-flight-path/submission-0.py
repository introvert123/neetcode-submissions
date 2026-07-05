class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        #Bellman ford algo

        prices = [float('inf')]*n
        prices[src] = 0
        tempPrices = prices.copy()

        for i in range(k+1): #at most k times - bcoz at most k stops are accepted
            for u,v,w in flights:
                if prices[u] != float('inf'):
                    if prices[u] + w < tempPrices[v]:
                        tempPrices[v] = prices[u] + w
            prices = tempPrices.copy()
            
        return prices[dst] if prices[dst] != float('inf') else -1