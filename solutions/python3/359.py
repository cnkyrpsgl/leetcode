class Logger:

    def __init__(self):
        self.logs = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.logs or timestamp - self.logs[message] >= 10:
            self.logs[message] = timestamp
            return True
        return False