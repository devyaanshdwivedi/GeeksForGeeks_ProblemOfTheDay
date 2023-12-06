class Solution:    
    def uchiha_madara(self,naruto,baruto):
        c=0
        while naruto>0:
            
            kaguya=naruto%10
            if kaguya==baruto:
                c+=1
            naruto=naruto//10
        return c
        
    def countX(self,L,R,X):
        count=0
        for i in range(L+1,R):
            count+=self.uchiha_madara(i,X)
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        L,R,X=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.countX(L,R,X)
        print(ans) 
# } Driver Code Ends