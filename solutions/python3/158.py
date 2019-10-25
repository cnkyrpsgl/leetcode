"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""]*4
            read4(buf4)
            self.queue += buf4
            curr = min(len(self.queue), n-idx)
            for i in range(curr):
                buf[idx] = self.queue.pop(0)
                idx+=1
            if curr == 0:
                break 
        return idx
        