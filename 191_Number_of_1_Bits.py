'''
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).



Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Option 1: transfer the integer to binary string and then count the 1s (bin(n).count('1'))
        #Time Complexity : O(logn) n is the integer
        #Space Complexity : O(logn) n is the integer

        #Option 2: Bit manipulation
        #Time Complexity : O(logn)
        #Space Complexity : O(1)
        res = 0
        for i in range(32):
            if n & 1 == 1:
                res += 1
            n >>= 1
        return res

        #is the function is called many times, we can store the new key and value in a dictionary every time we run the function.
