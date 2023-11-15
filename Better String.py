#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python
class Solution:
    def countDistinctSubsequences(self, string):
        n = len(string)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        last_occurrence = {}
        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % mod

            if string[i - 1] in last_occurrence:
                dp[i] = (dp[i] - dp[last_occurrence[string[i - 1]] - 1] + mod) % mod

            last_occurrence[string[i - 1]] = i

        return (dp[n] - 1 + mod) % mod

    def betterString(self, str1, str2):
        count_str1 = self.countDistinctSubsequences(str1)
        count_str2 = self.countDistinctSubsequences(str2)

        if count_str1 >= count_str2:
            return str1
        else:
            return str2

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends