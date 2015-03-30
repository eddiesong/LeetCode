class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x]+1, i+1)
            dict[x] = i
            
            
test = Solution()
arr = [5, 1, 4, 7, 2, 3]
print test.twoSum(arr, 9)