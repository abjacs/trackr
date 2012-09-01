import time


class Repeatable(object):
    
    def __init__(self, interval, function):
        self.interval = interval
        self.function = function
    
    def start(self):
        while True:
            # seconds
            time.sleep(self.interval)
            self.function()
