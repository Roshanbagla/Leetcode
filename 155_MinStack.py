class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        """Insert element in stack."""
        self.stack.append(x)
        return self.stack

    def pop(self):
        """Pop the last entered element in stack."""
        if self.stack is not None:
            return self.stack.pop()
        else:
            return "The stack is empty"

    def top(self):
        """Get the top element."""
        length = len(self.stack)
        top = self.stack[length-1]
        return top

    def getMin(self):
        """Get the minimum element in the stack."""
        minimum = min(self.stack)
        return minimum


minStack = MinStack()
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
