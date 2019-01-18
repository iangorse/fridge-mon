import os
import time
import subprocess
import polomail
import json


# Load the config file
with open("config.json") as json_data:
    config = json.load(json_data)

DEBUG           = False                 # Print debugging information

HOSTNAME 	= config["server"]	# Hostname to check for uptime
MIN_TIME 	= 60*5  		# Minimum time before being notificed in seconds (60*5 = 5 minutes)
is_down 	= False 		# flag to indicate if the current status is up or down
send_email	= True 		        # flag to indicate when to send notification - this avoids sending too many
start_time      = 0

# Avoid waiting 5 minutes just to test the script. If debbuging, reduce to 10 seconds
if DEBUG:
    MIN_TIME = 10

while True:
    ##############################################
    ## Ping the server I want to check is alive
    ## I do this with the subprocess module
    ## as I am not interested in seeing the output
    ## I only care about the return code
    ##############################################
    try:
        response = subprocess.check_output( ['ping', '-c', '3', 'rpi-fridge'],
                stderr=subprocess.STDOUT,
                universal_newlines=True
                )
    except subprocess.CalledProcessError:
        response = None
    
    ##############################################
    ## If there is a response then that means 
    ## the server is up. 
    ## Here I want to notify me that is has 
    ## come back up if it was previously down
    ##############################################
    if response:
        if is_down == True:
            is_down = False
            send_email = True
            current_time = time.time()
            elapsed = int(current_time - start_time)
            e = polomail.Email(config)
            e.sendEmail("Fridge has come back on.\n\nIt was off for %d minutes" % (elapsed/60), "Fridge Update - On")

    else:
    	#####################################################
    	## If it has gone down, then mark the time it started
    	#####################################################
    	if is_down == False:
    		is_down = True
    		start_time = time.time()
    	else:
    		#################################################
    		## If the server is still down, then check how
    		## much time has passed.
    		## I don't wan't false alarms, so I only need to
    		## be notified after MIN_TIME seconds has elapsed
    		#################################################
    		current_time = time.time()
    		if int(current_time - start_time) > MIN_TIME:
    			if send_email:
    				e = polomail.Email(config)
    				e.sendEmail("It looks like Dexter has switched the fridge off.\n\nGo and have a look", "Fridge Update - Off")		
    				send_email = False

    if DEBUG:
        print("is_down: %s, send_email: %s" % (is_down, send_email))  			

    time.sleep(30)

