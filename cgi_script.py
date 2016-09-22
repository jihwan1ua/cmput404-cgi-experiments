#!/usr/bin/env python

# importing python module
import cgi
import os
import json
import sys

form = cgi.FieldStorage()
loggedinok = False
# check username and password
if form.getvalue('user') == 'bob' and form.getvalue('password') == 'hunter2':
	loggedinok = True

if 'loggedin=true' in os.environ['HTTP_COOKIE']:
	loggedinok = True

# you can erase the cookie but then you can steal their cookie
# then type under console
# document.cookie = "loggedin=true";

# need to make this script executable by
# chmod +x cgi_script.py
print "Content-type: text/html"
# setting up the cookie, Set-Cookie is the http header
if loggedinok:
	print "Set-Cookie: loggedin=true"

print
print "<HTML><BODY><H1>Hello, World!</H1>"
print "<FORM method = 'POST'><INPUT name = 'user'/>"
print 	"<INPUT name ='password' type='password'>"
print 	"<BUTTON type='submit'>Log in</BUTTON>"
print "</FORM>"
print "<P>Query string was: " + os.environ['QUERY_STRING'] + "</P>"
print "<P>Your browser is: " + os.environ['HTTP_USER_AGENT'] + "</P>"
#if os.environ['CONTENT_LENGTH']:
	#print "<P>Standard Input is: " + sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
	#print "</P>"
#print "<P>"
#print "User name was: " + form.getvalue('user') + ". "
#print "Password was: " + form.getvalue('password') + ". "
#print "</P>"
if loggedinok:
	print "<H2> LOG IN OK! </H2>"


cgi.print_environ()

print json.dumps(dict(os.environ), indent=4)


print "</BODY></HTML>"