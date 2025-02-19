class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(prefix, n, k):
            if n == 0:
                return prefix
            for ch in 'abc':
                if prefix and ch == prefix[-1]:
                    continue
                cnt = 2 ** (n2 - len(prefix) - 1)
                if cnt >= k:
                    return dfs(prefix + ch, n - 1, k)
                else:
                    k -= cnt
            return ""
        
        n2 = n
        return dfs("", n, k)
