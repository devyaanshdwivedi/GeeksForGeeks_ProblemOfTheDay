class Solution:
    def columnWithMaxZeros(self, arr, N):
        max_zeros = 0
        max_zeros_column = -1

        for j in range(N):
            zeros_count = 0
            for i in range(N):
                if arr[i][j] == 0:
                    zeros_count += 1

            if zeros_count > max_zeros:
                max_zeros = zeros_count
                max_zeros_column = j

        return max_zeros_column


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends