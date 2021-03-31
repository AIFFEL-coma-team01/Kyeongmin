# 232. Implement Queue using Stacks
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        element = self.stack[0]
        self.stack.pop(0)
        return element
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0