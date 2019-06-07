class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        val = abs(x)
        i = 0
        while True:
            if(result < (-2**31) or result >(2**31-1)):
                return 0
            lstdgt = val % 10
            if val // 10 == 0:
                result += lstdgt
                break
            result = (result + lstdgt) * 10
            val = val // 10
        
        return result if x >= 0 else result * -1
            