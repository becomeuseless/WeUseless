'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #attemp 1: for every number smaller than n+1, check if it is a prime. To check if a number p is a prime, see if it                 #divisible by the numbers smaller than p.
        #Time Complexity : O(n**2)
        #Space Complexity : O(1)
        '''
        cnt = 0
        for i in range(1,n):
            if self.isPrime(i):
                cnt += 1
        return cnt

    def isPrime(self, x):
        if x == 1:
            return False
        for i in range(2,x):
            if x%i == 0:
                return False
        return True
        '''
        #attemp 2:To check if a number is p is a prime, we dont need to divide it by all the numbers smaller than p. Actually only
        #the numbers smaller than p**1/2 would be enough.
        #Time Complexity : O(n**1.5)
        #Space Complexity : O(1)
        '''
        cnt = 0
        for i in range(1,n):
            if self.isPrime(i):
                cnt += 1
        return cnt

    def isPrime(self, x):
        if x == 1:
            return False
        i = 2
        while i <= x**0.5:
            if x%i == 0:
                return False
            i += 1
        return True
        '''
        #attemp 3:When check if a number is a prime number, we will know for sure the multiples of the number are not prime numbers.
        #Thus we dont need to check the multiples.
        #Time Complexity : O(loglogn)
        #Space Complexity : O(n)
        if n < 3:
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False

        for i in range(int(n**0.5) + 1):
            if not isPrime[i]:
                continue
            j = i*i
            while j< n:
                isPrime[j] = False
                j += i
        return sum(isPrime)
