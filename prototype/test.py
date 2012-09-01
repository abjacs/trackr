from inet import Inet
from utils.repeatable import Repeatable

def blah():
    print Inet.get_router_mac_addy()

if __name__ == "__main__":
    timer = Repeatable(3, blah)
    timer.start()
