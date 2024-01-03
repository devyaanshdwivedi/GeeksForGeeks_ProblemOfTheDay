#User function Template for python3

class Solution:
    def smallestSubstring(self, s):
        # Code here
        hmap = {"0":0 , "1": 0, "2":0}
        i = 0 
        j = 0
        n = len(s)
        ans = float("inf")
        if n < 3:
            return -1 
        while(j < n or i < j):
            if ans == 3:
                return 3
            # print(hmap)
            if 0 in hmap.values():
                if j < n:
                    hmap[s[j]] += 1
                    j+=1
                else:
                    break
            if 0 not in hmap.values():
                ans = min(ans, j-i)
                hmap[s[i]] -= 1
                i+=1
                
        return ans if ans != float("inf") else -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends