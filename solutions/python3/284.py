# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self.bool = self.it.hasNext()
        self.num =  self.it.next() if self.bool else None
    def peek(self):
        return self.num

    def next(self):
        n = self.num
        self.bool = self.it.hasNext()
        if self.bool:
            self.num = self.it.next()
        return n

    def hasNext(self):
        return self.bool