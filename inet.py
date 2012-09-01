#!/usr/bin/env python
# encoding: utf-8

import os
import subprocess
import re


class Inet(object):
    
    @staticmethod
    def get_router_mac_addy():
        gateway = Inet.__get_default_gateway()
        mac = None
        
        if(gateway):
            arp_output =  subprocess.check_output(["arp", "-n", gateway])
            mac_regex = r"([0-9A-F]{1,2}[:-]){5}([0-9A-F]{2})"

            mac = re.search(mac_regex, arp_output, re.I).group()
        
        return mac
        
    @staticmethod
    def __get_default_gateway():
        cmd = "route -n get default"
        output = subprocess.check_output(["route", "-n", "get", "default"])
        
        gateway = None
        for line in output.split("\n"):
            if(line.find("gateway") >= 0):
                gateway = line.replace("gateway:", "").strip()
                break

        return gateway

if __name__ == "__main__":
    print Inet.get_router_mac_addy()
