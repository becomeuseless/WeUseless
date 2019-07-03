"""
17. Letter Combinations of a Phone Number

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        My thoughts:
        For each digits, find each possible letter from array and goes to next letter array combine all until no element left
        then add the combination into the dictionary
        
        Base case:
            all number are used
            
        Time: O ( (3)^n2 * 3^n3 *....4^n9) < 4^(n1+n2+n3+...+n9) n2=number count of 2
        Space: O ( (3)^n2 * 3^n3 *....4^n9) < 4^(n1+n2+n3+...+n9) n2=number count of 2 )
        """
        if not digits:
            return []
        pad = ['', '', 'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        result = []
        cache = ''
        self.resolver(cache, digits, result, pad)
        return result
    
    def resolver(self, cache, notResolved, result, pad):
        if len(notResolved) == 1:
            for each in pad[int(notResolved[0])]:
                result.append(cache + each)
        else:
            for each in pad[int(notResolved[0])]:
                self.resolver(cache + each, notResolved[1:], result, pad)
                

            
