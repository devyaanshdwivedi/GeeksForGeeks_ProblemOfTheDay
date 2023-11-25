class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        p=n//2
        j=1
        for i in range(p,n):
            s=arr.pop(i)
            arr.insert(j,s)
            j+=2
        return arr


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends