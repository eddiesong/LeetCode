class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        MaxSum = -32767
        HereSum = 0
        
        for item in A:
            if HereSum <= 0:
                HereSum = item
            else:
                HereSum = HereSum + item
            
            if HereSum > MaxSum:
                MaxSum = HereSum
                
        return MaxSum