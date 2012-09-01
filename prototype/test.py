from inet import Inet
from utils.repeatable import Repeatable

def blah():
    from datetime import datetime
    print "%s (%s)" % (Inet.get_router_mac_addy(), datetime.today())

if __name__ == "__main__":
    timer = Repeatable(3, blah)
    timer.start()
