class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                current_prod = nums1[i - 1] * nums2[j - 1]
                
                # Choices:
                # 1. Take current pair only
                # 2. Take current pair + previous best
                # 3. Don't take current pair, keep best from nums1 prefix
                # 4. Don't take current pair, keep best from nums2 prefix
                
                dp[i][j] = max(
                    current_prod,
                    current_prod + dp[i - 1][j - 1],
                    dp[i - 1][j],
                    dp[i][j - 1]
                )
        
        return dp[n][m]