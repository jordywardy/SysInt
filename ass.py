#!/usr/bin/env python2.7

from cmd import Cmd
import os, pwd, time, getpass, pass_file, grp, ipconfig_file

class Ass(Cmd):
	def do_pw(self, args):
		print("This is the current directory:")
		pass_file.Dir()

	def do_ifc(self, args):
		if (args == ""):
			print("This is the information for eth0")
		else:
			print"This is the information for",args
		ipconfig_file.eth(args)
	
	def do_date(self, args):
		print("Today's date and time is as follows")
		print(time.strftime("%Y%m%d%H%M%S"))

	def do_leave(self, args):
                print("Goodbye...")
                time.sleep(2.5)
                os._exit(1)

	def do_user(self, args):
		usr = getpass.getuser()
		usrID = pwd.getpwnam(usr).pw_uid
		groupID = pwd.getpwnam(usr).pw_gid
		groupName = grp.getgrgid(groupID).gr_name
	
		homeDir = os.getenv("HOME")
		homeDirInfo = os.stat(homeDir)
		iNode = homeDirInfo.st_ino

		print(str(usrID))
		print(str(groupID))
		print(usr)
		print(groupName)
		print(str(iNode))

ass1 = Ass()

ass1.prompt = '--> '

ass1.cmdloop('And so it begins...')
