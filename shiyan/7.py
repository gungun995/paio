MOD = 1000000007

def num_ids(n, l):
    dp = [0] * (l+1)
    dp[0] = 1

    for i in range(1, l+1):
        curr = 0
        for j in range(n):
            curr += dp[i-1]
            curr %= MOD
        dp[i] = curr

    return sum(dp) % MOD

while True:
    try:
        n, l = map(int, input().split())
        print(num_ids(n, l)-1)
    except:
        break