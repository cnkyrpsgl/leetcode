import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.z = threading.Semaphore()
        self.e = threading.Semaphore()
        self.o = threading.Semaphore()
        self.e.acquire()
        self.o.acquire()
        self.cur = 1
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.z.acquire()
            printNumber(0)
            if self.cur % 2:
                self.o.release()
            else:
                self.e.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.e.acquire()
            printNumber(self.cur)
            self.cur += 1
            self.z.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2 + self.n % 2):
            self.o.acquire()
            printNumber(self.cur)
            self.cur += 1
            self.z.release()