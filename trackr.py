import os
import datetime
import pickle
import inet


def setup():
	print "Gathering router MAC address"
	
	router_mac_address = inet.get_router_mac_addy()
	
	#persist to current user directory as hidden file
	home = os.getenv("HOME")
	filename = ".trackr"
	filename = os.path.join(home, filename)
	
	#check if exists
	if(not os.path.exists(filename)):
		print "Initializing on first run..."
		print "Please answer some questions to help me setup. ;-)"
		f = open(filename, "w")
		
		question = "Where are you running this from:"
		choices = """
		a) work?
		b) home?
		c) other?
		
		"""
		question += choices
		
		valid_responses = {
			"a" : "work",
			"b" : "home",
			"c" : "other"
		}
		
		resp = raw_input(question.strip()).lower()
		location = {
			"work" : "",
			"home" : "",
			"other" : ""
		}
		
		if(resp in valid_responses.keys()):
			loc = valid_responses[resp]
			location[loc] = router_mac_address
			
			print "Saving MAC address %s for %s" % (router_mac_address, loc)		
		else:
			print "Repeating the question...choose a, b, or c."
		
		pickle.dump(location, f)
		f.close()
	else:
		print "Load 'er up..."


if __name__ == "__main__":
	setup()

	home = os.getenv("HOME")
	filename = ".trackr"
	filename = os.path.join(home, filename)
	f = open(filename, "r")
	location = pickle.load(f)
	f.close()
	
	print location