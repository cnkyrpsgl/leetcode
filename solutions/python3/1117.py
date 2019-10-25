from threading import Lock

class H2O(object):
    def __init__(self):
        self.H = 0
        self.O = 0
        self.mu = Lock()
        pass


    def hydrogen(self, releaseHydrogen):
        self.releaseHydrogen = releaseHydrogen
        with self.mu:
            self.H += 1
            self.ouput()

    def oxygen(self, releaseOxygen):
        self.releaseOxygen = releaseOxygen
        with self.mu:
            self.O += 1
            self.ouput()
        
    def ouput(self):
        while self.ok():
            self.releaseHydrogen()
            self.releaseHydrogen()
            self.releaseOxygen()
            self.H -= 2
            self.O -= 1
    
    def ok(self):
        return self.H >= 2 and self.O >= 1