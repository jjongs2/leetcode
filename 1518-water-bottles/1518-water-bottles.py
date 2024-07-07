class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk_count = numBottles
        while numBottles >= numExchange:
            exchanged = numBottles // numExchange
            drunk_count += exchanged
            numBottles = exchanged + numBottles % numExchange
        return drunk_count
