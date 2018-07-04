# Write a program to get formatted time.

import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
