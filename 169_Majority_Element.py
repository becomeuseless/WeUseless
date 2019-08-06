'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Option 1: loop thru the list. Time will be O(n), Space can be O(n/2)
        #Option 2: sort the list and then get the middle element. Time will be O(nlogn), space is O(1)
        #Option 3: there is this smart algorithm that does one pass with a O(1) space.

        majority, count = nums[0], 0
        for n in nums:
            if count == 0:
                majority, count = n, 1
            elif majority == n:
                count += 1
            else :
                count -= 1
        return majority

    """
    Using Hashmap
    Counter is a subclass of dictionary object. The Counter() function in collections                   module takes an iterable or a mapping as the argument and returns a Dictionary.             In this dictionary, a key is an element in the iterable or the mapping and                 value is the number of times that element exists in the iterable or the                     mapping.
    defaultdict
    OrderedDict
    deque
    ChainMap
    namedtuple()
    
    More details: https://stackabuse.com/introduction-to-pythons-collections-module/
    """
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
    
    """
    There are 4 more ways resolve this. Fk off.
    O(N)
    """
    def majorityElement1(self, nums: List[int]) -> int:
        memo = {}
        for each in nums:
            if each in memo:
                memo[each] += 1
            else:
                memo[each] = 1
            #check if it's majority    
            if memo[each] > len(nums) / 2:
                return each
            
        return 0
