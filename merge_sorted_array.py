class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        tmp = [0 for i in range(m+n)]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                tmp[k] = A[i]
                i += 1
            else:
                tmp[k] = B[j]
                j += 1
            k += 1
        if i == m:
            while k < m+n:
                tmp[k] = B[j]
                j += 1
                k += 1
        else:
            while k < m+n:
                tmp[k] = A[i]
                i += 1
                k += 1
        for i in range(m+n):
            A[i] = tmp[i]