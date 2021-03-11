# 622. Design Circular Queue

class MyCircularQueue(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.idx = k
        self.cir = []
        self.rear = -1
        self.front = 0
        
    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        # rear ++
        if len(self.cir) == self.idx:
            return False
        
        self.cir.append(value)
        self.rear += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        # rear --
        # print(self.cir)
        if len(self.cir) == 0:
            return False
        self.cir.pop(0)
        self.rear -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if len(self.cir) == 0:
            return -1
        return self.cir[self.front]
        
    def Rear(self):
        """
        :rtype: int
        """
        # print(self.cir)
        # print(self.rear)
        if len(self.cir) == 0:
            return -1
        return self.cir[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.cir) == 0
    

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.cir) == self.idx
