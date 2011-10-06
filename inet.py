#!/usr/bin/env python
# encoding: utf-8

import os

output = ""

def __get_default_gateway():
	cmd = "route -n get default"
	output = os.popen("route -n get default").readlines()
	
	gateway = ""
	for line in output:
		if(line.find("gateway") >= 0):
			gateway = line.replace("gateway:", "").strip()
			break
			
	return gateway
	
def get_router_mac_addy():
	gateway = __get_default_gateway()
	cmd = "arp -n %s"
	cmd = cmd % gateway
	
	arp_output =  os.popen(cmd).readlines()[0]
	import re
	mac_regex = r"([0-9A-F]{1,2}[:-]){5}([0-9A-F]{2})"
	
	mac = re.search(mac_regex, arp_output, re.I).group()
	return mac
	
if __name__ == "__main__":
	print get_router_mac_addy()