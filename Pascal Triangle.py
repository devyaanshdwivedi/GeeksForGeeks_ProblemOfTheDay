#User function Template for python3

#User function Template for python3

class Solution:
    def nthRowOfPascalTriangle(self,n):
        # code here
        mod = 10**9+7
        res = [1]*n
        for i in range(1, n):
            for j in range(i-1, 0, -1):
                res[j] = (res[j] + res[j-1]) % mod
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends