'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):

#the minimun can be stored in every element and because of stack's feature, the last element will always keep the #current minimum value.
#Time Complexity : push O(1) pop O(1) top O(1) GetMin O(1)
#Space Complexity : push O(1) pop O(1) top O(1) GetMin O(n) in order to store min in every element.

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        try :
            self.item.append([x, min(x,self.item[-1][1])])
        except :
            self.item.append([x,x])


    def pop(self):
        """
        :rtype: None
        """
        self.item.pop()



    def top(self):
        """
        :rtype: int
        """
        return self.item[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        return self.item[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
