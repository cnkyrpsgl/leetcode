import threading
class Foo(object):
    def __init__(self):
        self.two = threading.Semaphore()
        self.three = threading.Semaphore()
        self.two.acquire()
        self.three.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.two.release()
		
    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.two.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.three.release()
        
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.three.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()