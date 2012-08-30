from datetime import datetime

class Events(object):
    
    def __init__(self):
        self.lastKeyPress = 0
        self.lastMouseMovement = 0
        
    def lastKeyPress(self):
        return self.lastKeyPress
        
    def lastMouseMovement(self):
        return
    
    def start(self):
        while 1:
            if(Events.__heardKeyboard()):
                self.lastKeyPress = datetime.now()
            else:
                self.lastKeyPress = 0
    
    @staticmethod
    def __heardKeyboard():
        i,o,e = select.select([sys.stdin],[],[],0.0001)
        for s in i:
            if s == sys.stdin:
                input = sys.stdin.readline()
                return True
        return False


if __name__ == "__main__":
    print "Last key press: %s" % 'n/a'
    print "Last mouse movement: %s" % 'n/a'