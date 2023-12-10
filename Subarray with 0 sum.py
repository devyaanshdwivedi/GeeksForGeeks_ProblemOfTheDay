#User function Template for python3

class Solution:
    
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr, n):
        # Your code here
        # Return true or false
        
        # Initialize an empty set to store the prefix sums
        prefix_sum_set = set()
        
        # Initialize a variable to store the running sum
        running_sum = 0
        
        # Iterate through the array
        for i in range(n):
            # Add the current element to the running sum
            running_sum += arr[i]
            
            # If the running sum is 0 or if it has been seen before, there is a subarray with sum 0
            if running_sum == 0 or running_sum in prefix_sum_set:
                return True
            
            # Add the running sum to the set
            prefix_sum_set.add(running_sum)
        
        # If no subarray with sum 0 is found
        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends