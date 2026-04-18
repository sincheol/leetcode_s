class Solution:
    '''
    len(coins) 가 매우 작음
    -> dp일가능성
    제일 큰수부터 시작해서 dp로 서치하고
    만약 실패한다면 그 다음 작은 수로 dp로 서치하면
    근데 그것도 있네 무조건 큰거에서 최대로 빼내는게 좋은게 아니고 작게 해서 완성시키는 것도 있을 수 있음

    그렇다면 그냥 coin의 작은 수부터 amount까지 올라가면서 갯수를 업데이트해가는거
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)

        if dp[amount] == amount+1:
            return -1
        return dp[amount]
        