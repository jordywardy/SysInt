#!/usr/bin/env python2.7

from cmd import Cmd
import os, pwd, time, getpass, pass_file, grp, ipconfig_file

class Ass(Cmd):
	answer = "0"
	def do_pw(self, args):
		print("This is the current directory:")
		pass_file.Dir()
		print("Choose an option: pw|date|user|ifc|leave")

	def do_ifc(self, args):
		if (args == ""):
			print("This is the information for eth0")
		else:
			print"This is the information for",args
		ipconfig_file.eth(args)
		print("Choose an option: pw|date|user|ifc|leave")
	
	def do_date(self, args):
		print("Today's date and time is as follows")
		print(time.strftime("%Y%m%d%H%M%S"))
		print("Choose an option: pw|date|user|ifc|leave")

	def do_leave(self, args):
		print("Are you sure you wish to leave? y/n")
		answer = raw_input()
		if (answer == "y"):
                	print("Goodbye...")
                	time.sleep(2.5)
               		os._exit(1)
		if (answer == "n"):			
			ass1 = Ass()
			ass1.prompt = '-->'
			print("Choose an option: pw|date|user|ifc|leave")

	def do_user(self, args):
		print("This is all the user information")
		usr = getpass.getuser()
		print "User: ",usr
		usrID = pwd.getpwnam(usr).pw_uid
		print "User ID: ",str(usrID)
		groupID = pwd.getpwnam(usr).pw_gid
		print "Group ID: ",str(groupID)
		groupName = grp.getgrgid(groupID).gr_name
		print "Group Name: ",groupName
		homeDir = os.getenv("HOME")
		homeDirInfo = os.stat(homeDir)
		iNode = homeDirInfo.st_ino
		print "iNode: ",str(iNode)
		print("Choose an option: pw|date|user|ifc|leave")

ass1 = Ass()
ass1.prompt = '--> '
ass1.cmdloop("Choose an option: pw|date|user|ifc|leave")
