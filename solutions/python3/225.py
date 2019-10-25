class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.data.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.data[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not bool(self.data)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()