#!/usr/bin/python3 

import cgi
import subprocess as sb

print("content-type: text/html")
print()


a = cgi.FieldStorage()
cmd = a.getvalue("x")

#print(cmd)

x = sb.getoutput("sudo " + cmd)
#x = sb.getoutput(cmd)
print(x)
