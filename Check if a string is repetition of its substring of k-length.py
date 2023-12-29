#User function Template for python3
class Solution:
    def kSubstrConcat(self, n, s, k):
        # Your Code Here
        if n % k > 0:
            return 0

        mp = {}
        for i in range(0, n // k):
            substr = s[i * k : (i + 1) * k]
            mp[substr] = mp.get(substr, 0) + 1

        cnt = sum(val > 1 for val in mp.values())
        return int(len(mp) <= 2 and cnt <= 1)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends