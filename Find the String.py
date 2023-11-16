#User function Template for python3

class Solution:
    def findString(self, N, K):
        # code here
        if N==1:
            return "".join([str(i) for i in range(K)])
        ans = "0"*N
        strs = {ans}
        while len(strs) < K**N:
            for i in range(K-1, -1, -1):
                if ans[-N+1:]+str(i) not in strs:
                    strs.add(ans[-N+1:]+str(i))
                    ans += str(i)
                    break
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())

        ob = Solution()
        ans = ob.findString(N,K)
        ok = 1
        for i in ans:
            if ord(i)<48 or ord(i)>K-1+48:
                ok = 0
        if not ok:
            print(-1)
            continue
        d = dict()
        i = 0
        while i+N-1<len(ans):
            d[ans[i:i+N]] = 1
            i += 1
        tot = pow(K,N)
        if len(d)==tot:
            print(len(ans))
        else:
            print(-1)
# } Driver Code Ends