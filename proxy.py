import os
import sys
print '\033]2;BoOoter | Proxy | @tuf_unkn0wn\a'

def start():
	os.system("service tor start")
	os.system("proxychains python boOoter.py")

def no():
	print "Exiting..."
	print "Follow @tuf_unkn0wn on instagram"
	sys.exit()

print """the proxy.py file runs boOoter with proxychains
note some things might not work or might be slow to run
"""
print "\nWould you like to run proxy?\n"
yn = raw_input("[y/n]-> ")
if yn == "y":
	start()
if yn == "yes":
	start()
if yn == "n":
	no()
if yn == "no":
	no()
