class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        red_count = 0
        white_count = 0
        
        for item in A:
            if item == 0:
                red_count += 1
            elif item == 1:
                white_count += 1
        
        for i in range(red_count):
            A[i] = 0
        for i in range(red_count, red_count + white_count):
            A[i] = 1
        for i in range(red_count + white_count, len(A)):
            A[i] = 2