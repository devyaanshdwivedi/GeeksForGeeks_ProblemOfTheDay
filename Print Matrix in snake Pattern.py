
#User function Template for python3

class Solution:
    # Function to return a list of integers visited in a snake pattern in the matrix.
    def snakePattern(self, matrix):
        n = len(matrix)
        snake_pattern = []

        for i in range(n):
            # For even rows, add elements from left to right
            if i % 2 == 0:
                for j in range(n):
                    snake_pattern.append(matrix[i][j])
            # For odd rows, add elements from right to left
            else:
                for j in range(n - 1, -1, -1):
                    snake_pattern.append(matrix[i][j])

        return snake_pattern
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends