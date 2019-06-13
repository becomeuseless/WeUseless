'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

## use dictionary and stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydict = {}
        mydict[']'] = '['
        mydict[')'] = '('
        mydict['}'] = '{'
        mystack = []
        for item in s :
            if item in mydict.values() :
                mystack.append(item)
            if item in mydict.keys() :
                if mystack == [] :
                    return False
                elif mystack[-1] == mydict[item] :
                    mystack.pop()
                else :
                    return False

        return mystack == []

    def isValid2(self, s: str) -> bool:
        """
        20. Valid Parentheses
        O(n): time
        O(n): Space
        """
        if len(s) == 0:
            return True
        stack = []
        for each in s:
            if each == "(" or each == "[" or each =="{":
                stack.append(each)
                continue
            if each == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop()         
            if each == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                stack.pop()
            if each == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False