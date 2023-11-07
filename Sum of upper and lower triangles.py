
#User function Template for python3

class Solution:
    def sumTriangles(self, matrix, n):
        sum_upper = 0
        sum_lower = 0

        for i in range(n):
            for j in range(i, n):
                sum_upper += matrix[i][j]

        for i in range(n):
            for j in range(0, i + 1):
                sum_lower += matrix[i][j]

        return [sum_upper, sum_lower]



        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]

        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        ans = obj.sumTriangles(matrix, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends