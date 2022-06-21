class Solution:
    def maxProfit(self, prices) -> int:
        size = len(prices)

        if size == 0 or size == 1:
            return 0

        results = [0]*size

        if size > 1:
            results[1] = max(prices[1]-prices[0], 0)
                
        for i in range(2, size):
            results[i] = max(list(map(lambda x: max(prices[i]-prices[x] + results[x-2], 0, results[i-1]) if x > 2 else max(prices[i]-prices[x], 0, results[i-1]), (ii for ii in range(0, i)))))
            print(results[i])

        return results[-1]

tmp = Solution()
print(tmp.maxProfit([1, 2, 4]))