#User function Template for python3

class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        seen = set()
        ans = []
        for i in range(m):
            t = tuple(arr[i])
            if t in seen:
                ans.append(i)
            seen.add(t)
        return ans
