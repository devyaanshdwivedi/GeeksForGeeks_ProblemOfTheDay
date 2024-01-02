#User function Template for python3

class Solution():
    def maxSumWithK(self, a, n, k):
        kWinSum = 0
        for i in range(k):
            kWinSum += a[i]
        
        currSum = kWinSum
        maxSum = kWinSum
        for j in range(k,n):
            i = j-k
            kWinSum = kWinSum + a[j] - a[i]
            currSum = max(kWinSum , currSum + a[j])
            maxSum = max(maxSum,currSum)
        return maxSum
            
        
    
    
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends