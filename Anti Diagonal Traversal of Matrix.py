#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        n=len(matrix)
        m=len(matrix[0])
        col=0
        row=0
        ans=[]
        while (col<m and row<n):
            i=col
            j=row
            while (i>=0 and j<n ):
                ans.append(matrix[j][i])
                i-=1
                j+=1
            if(col<m-1):
                col+=1
            else:
                row+=1
        return ans
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends