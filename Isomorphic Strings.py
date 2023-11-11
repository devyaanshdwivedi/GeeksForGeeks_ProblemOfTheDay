class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self, str1, str2):
        if len(str1) != len(str2):
            return False
        
        mapping_dict = {}
        visited_chars = set()
        
        for i in range(len(str1)):
            char1 = str1[i]
            char2 = str2[i]
            
            # If char1 is already mapped, it should be mapped to char2.
            if char1 in mapping_dict:
                if mapping_dict[char1] != char2:
                    return False
            else:
                # If char1 is not mapped, but char2 is already used, then it's not isomorphic.
                if char2 in visited_chars:
                    return False
                
                # Create a mapping from char1 to char2.
                mapping_dict[char1] = char2
                visited_chars.add(char2)
        
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends