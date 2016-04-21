from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import sys
import time
import win32gui
import subprocess
import urllib2


############################################################
# Enter your Firewall Credentials Here                     #
############################################################
#                                                          #
USER_NAME = ''	# Fill in your username                       
PASSWORD  = ''	# Fill in your password   
#                                                          #
############################################################


############################################################
# Variables                                                #
############################################################
#                                                          #
AUTH_URL   = "https://172.17.100.100:8443/auth1.html"
NCSI_URL   = "http://www.msftncsi.com/ncsi.txt"
LOGOUT_URL = "https://172.17.100.100:8443/dynLoggedOut.html"
#                                                          #
############################################################

# Check if Internet connection is active
def check_for_active_internet():
	try:
		response = urllib2.urlopen(NCSI_URL)
		source   = response.read()
		if len(source) is 14:
			return True
		else:
			return False
	# SonicWall is beautiful in Amrita, as you know. Any failed attempt will give handshake error even on HTTP due to redirection 
	except:
		return False

#The heart, brain and kidney of the script
def main() :
	driver = webdriver.Firefox()	
	driver.set_window_position(-2000, 0)
	driver.set_window_size(50, 50)
	driver.set_page_load_timeout(15) 

	print "\n\n[*]  Opening a New Session.."
	try :
		driver.get(AUTH_URL)
	except TimeoutException:
		print "[!] Target can't be reached. Are you on the right WiFi / Are you using a proxy?"
		driver.quit()
		return
	assert "Sonic" in driver.title
	print "\n\n[*] Enumerating Login Page.."

	user = driver.find_element_by_name("userName")
	passwd = driver.find_element_by_name("pwd")

	print "\n\n[*] Sending Credentials .. "
	user.send_keys(USER_NAME)
	passwd.send_keys(PASSWORD)
	passwd.send_keys(Keys.RETURN)

	# A URL needs to be accessed after login to keep the internet active 	
	driver.get(NCSI_URL)
	if not check_for_active_internet():
		print "\n\n[!] Could not Login! Invalid Credentials / Account already in Use!"
		driver.quit()
		return 1
	print "\n\n[*] Login Done! Will repeat in an hour."
	driver.quit()

	# The program will sleep for a little less than 1 hour. 
	time.sleep((60 * 60) - 5 )

# Forever and ever, until a Keyboard Interrupt is encountered
while True :
	try :
		error_value = main()
		if error_value == 1 : 
			break
	except KeyboardInterrupt:
		print "\n\n ~~~~Enough Internet for Today! ~~~~~"
		sys.exit()

