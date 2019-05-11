class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.order = 1
        self.B = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.B.append(val)
        length = len(self.B)
        if length <= self.size:
            average = float((sum(self.B))/length)
            return average
        else:
            self.B = self.B[self.order:]
            self.order = self.order + 1
            print (self.B)
            length = len(self.B)
            average = float((sum(self.B))/length)
            return (average)

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
param_1 = obj.next(1)
param_2 = obj.next(5)
param_3 = obj.next(10)
param_4 = obj.next(20)
print(param_4)
param_5 = obj.next(24)
print(param_5)
