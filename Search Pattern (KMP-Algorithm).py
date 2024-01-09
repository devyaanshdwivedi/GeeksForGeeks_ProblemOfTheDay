#User function Template for python3

class Solution:
    def search(self, pat, txt):
        n = len(txt)
        p = len(pat)
        i = s = 0
        res = []
        while (s < n):
            i = s
            if txt[i] == pat[0]:
                start = i
                j = 0
                while j < p and i < n and txt[i] == pat[j]:
                    i += 1
                    j += 1
                if j == p :
                    res.append(start + 1)
            s += 1
            
        return res
                
