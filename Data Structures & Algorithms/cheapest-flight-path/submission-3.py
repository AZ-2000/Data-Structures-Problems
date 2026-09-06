class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("infinity")] * n
        prices[src] = 0

        for i in range(k+1):
            tmp = prices[:]
            for source, destination, price in flights:
                if price == float("infinity"):
                    continue
                if prices[source] + price < tmp[destination]:
                    tmp[destination] = prices[source] + price
            prices = tmp[:]
        
        if prices[dst] == float("infinity"):
            return -1
        else:
            return prices[dst]


