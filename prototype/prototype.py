from inet import Inet


if __name__ == "__main__":
    
    # grab mac address
    mac = Inet.get_router_mac_addy()
    if(mac == None):
        print "Unable to retrieve route MAC address"
    #else
    
    # look for mac in our DB
    
    # found in DB?...log time
    
    # not found in DB?...ask user what this place is
    
    # periodically log MAC address