class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        i = 0
        sign = 1
        result = 0
        if str == '':
            return 0
        while i < len(str) and str[i].isspace():
            i+=1
        if i < len(str) and str[i] == '-':
            sign = -1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i += 1
        while i < len(str) and str[i].isdigit():
            result = result * 10 + int(str[i])
            i += 1
        
        if result*sign <= INT_MIN:
            return INT_MIN
        else:
            if result*sign >= INT_MAX:
                return INT_MAX
            else:
                return result*sign
        
            
test = Solution()
print test.atoi("   -2147483647")
        
        