#User function Template for python3

class Solution:
    def match(self, wild, pattern):
        # code here
        p,w,pstar,wstar,m,n=0,0,-1,-1,len(pattern),len(wild)
        wild+='_'
        while p<m:
            if pattern[p]==wild[w] or wild[w]=='?':
                p+=1
                w+=1
            elif wild[w]=='*':
                wstar=w
                w+=1
                pstar=p
            elif wstar>=0:
                w=wstar+1
                pstar+=1
                p=pstar
            else:
                return False
        while w<n:
            if wild[w]!='*':
                return False
            w+=1
        return True
