#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        hm = {}
        
        for i in arr:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
                
        
        mx = max(hm.values())
        v = []
        for i in hm:
            if hm[i] == mx:
                v.append(i)
                
                
                
        return sorted(v)[0], mx





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends