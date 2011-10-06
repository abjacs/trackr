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
		
		question = r"""
		Are you running this from:
			a) work?
			b) home?
			c) other?
		"""
		valid_responses = {
			"a" : "work",
			"b" : "home",
			"c" : "other"
		}
		
		resp = raw_input(question).lower()
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

#old code, which I may come back to one day (10/05/2011)
"""
		isWork = isWork()
		location = "your work" if isWork else "your home"
		resp = raw_input("I'm guessing that you're running from %s. Is this correct? (y/n)", % location).lower()
		
		#figure out if we're at work or home
		if(resp.lower() == "y"):
			isWork = True
		else if(resp.lower() == "n"):
			isWork = False
		else:
			print "Repeating the question..."
			
	else:
		f = open(filename, "rw")
		log = f.readlines()
				
	f.close()
	
def isWork():
	weekdays = [str(day) for day in range(1, 6)]
	work_hours = [str(hour) for hour in range(8, 18)]
	#check if weekday && if beween 8AM - 5PM
	now = datetime.datetime.now()
	day = now.strftime("%w")
	hour = now.strftime("%H")
	isWork = (day in weekdays and hour in work_hours)
	return isWork
"""