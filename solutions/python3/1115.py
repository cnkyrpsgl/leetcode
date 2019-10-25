import threading
class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.f = threading.Semaphore()
        self.b = threading.Semaphore()
        self.b.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            self.f.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.b.release()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.b.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.f.release()