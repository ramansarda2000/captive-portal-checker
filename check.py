# use python3

import socket, webbrowser, subprocess
from urllib.request import urlopen

url = 'http://connectivitycheck.gstatic.com/generate_204'
response = urlopen( url )

if response.getcode()==200:
	subprocess.Popen(['notify-send', "You need to log into the network."])
	webbrowser.open_new_tab('http://connectivitycheck.gstatic.com/generate_204')
else:
	subprocess.Popen(['notify-send',"Connected to internet.  All good :)"])
