def solution(n):
    dp = [0] * (n+1)
    dp[2] = 3
    dp[4] = 11
    
    for i in range(6, n + 1, 2):
        # 점화식
        # dp[n] = dp[n-2]*3 + dp[n-4]*2+dp[n-6]*2+...+dp[2]*2 + 2
        dp[i] = (3 * dp[i-2] + sum(dp[2:i-2]) * 2 + 2) % 1000000007
    
    return dp[n]