#!/usr/bin/env python
import time       				# for the pause
import random					# for random routines	
import sys 						# used for the system exit function 
from os import system 			# used for the clear function
from playsound import playsound # used to play the dialer sounds
import shelve					# used to save game


#load initial settings

def load_local_info():
		li={0:{'fname':'command.com','fdate':'13/04/86','fsize':'12,332'},
		1:{'fname':'dialer.exe','fdate':'15/11/87','fsize':'72,352'},
		2:{'fname':'zzmail.exe','fdate':'04/05/86','fsize':'14,343'},
		3:{'fname':'help.exe','fdate':'16/12/82','fsize':'1,632'},
		4:{'fname':'readme','fdate':'16/08/86','fsize':'457'},
		5:{'fname':'notes.exe','fdate':'23/01/84','fsize':'3,466'}}
		return li
		
def load_phone_numbers():
	pn={}
	for n in range(20):
		r3 = random.choice(range(1,9))*100000000+int(random.random()*100000000)
		p1=r3 / 10000000
		p2=(r3 - p1 * 10000000) / 10000
		p3=(r3 - (p1 * 10000000) - (p2 * 10000))
		part1=""
		part2=""
		part3=""
		part1=str(0)+str(p1)
		if p2<100:
			part2=str(0)
		if p2<10:
			part2=part2+str(0)
		part2=part2+str(p2)
		if p3<1000:
			part3=str(0)
		if p3<100:
			part3=part3+str(0)
		if p3<10:
			part3=part3+str(0)
		part3=part3+str(p3)
		#print n, r3, part1, part2, part3, p1, p2, p3
		pn[n]={}
		pn[n] ["real_number"] = str(0)+str(r3)
		pn[n] ["display_number"] = part1+" "+part2+" "+part3
	return pn	
	
def load_crypto_keys():
	ci=[]
	hexkey="0123456789ABCDEF"
	for o in range(10):
		enckey=""
		for n in range(8):
			m=int(random.choice(range(0,16)))
			enckey=enckey+hexkey[m]
		ci.append(enckey)
		#print enckey
	return ci
			 
def load_target_info():
	ti={0:{'tnumber':phone_info[0]['real_number'],'tsystem':"Wang VS 85 OS version 8.33",
			"tfiles":['0001.doc','0002.doc','0003.doc','pointer.doc']},
			1:{'tnumber':phone_info[1]['real_number'],'tsystem':"DEC PDP 11 OS version 3.476",
			"tfiles":['Proposal.TX','Callouts.FX','Personnel.LS','Phone.LS','Pointer.TX']},
			2:{'tnumber':phone_info[2]['real_number'],'tsystem':"IBM System 370-168 OS Mvs/VTAM",
			"tfiles":['Anomaly','Telephones','Staff','Enquiries']},
			3:{'tnumber':phone_info[3]['real_number'],'tsystem':"HONEYWELL 600 OS version 5.82a",
			"tfiles":['0002548.msg','0003674.msg','0008467.msg','0010005.msg','0010006.msg','0010007.msg','0012453.msg',
			'0012544.msg','0012555.msg','0012556.msg','0012557.msg']},
			4:{'tnumber':phone_info[4]['real_number'],'tsystem':"TDC 316 OS version 1.32",
			"tfiles":[tar_key[0]+'.TAR',tar_key[7]+'.TAR',tar_key[2]+'.TAR',tar_key[3]+'.TAR',tar_key[4]+'.TAR']},
			5:{'tnumber':phone_info[5]['real_number'],'tsystem':"CRAY Y-MP OS version 7.882",
			"tfiles":[]},
			6:{'tnumber':phone_info[12]['real_number'],'tsystem':"ACT SIRIUS 2 OS CP/M version 86",
			"tfiles":['MissBlack.ac']},
			7:{'tnumber':phone_info[14]['real_number'],'tsystem':"Burroughs 1440 OS version 12.0",
			"tfiles":[]},
			8:{'tnumber':phone_info[15]['real_number'],'tsystem':"Data General GEISCO OS version 3.45f",
			"tfiles":[]},
			9:{'tnumber':phone_info[16]['real_number'],'tsystem':"Nixdorf OS version 3.6D",
			"tfiles":[]}}
	return ti
 
def intro_screen():
	clear()
	print ("Hacker\n".center(60))
	print ("A text based game by Richard Tatschner\n\n".center(60))
	time.sleep(3)
	print ("In the 1980's before the Internet was released to the public,")
	print ("computers had to connect to each other over the telephone")
	print ("network by using a device called a Modem and a program called")
	print ("a dialer to dial the number that the target computer was hooked")
	print ("up to.\n")
	time.sleep(5)
	print ("This was the era of hacking. I have recreated the computer")
	print ("environment with it's limited set of tools to give you a flavour")
	print ("of those halcion days. Buckle up and enjoy the experience of")
	print ("hacking.\n")
	raw_input("Press Enter to continue...")
	clear()

def clear(): 
     _ = system('clear') 

def start_screen():
	print ("......booting")
	time.sleep(3)
	clear()
	time.sleep(2)
	print("Linux DOS 2.11 Generic RAM BIOS")
	print("Version R1.6 12/6/1986\n")
	print("Command ver 2.16st\n")
	print("Notebook version 2.2 [TSR] loaded.")
	print("(Numbers & keys autostored)\n")

def win_screen():
	print("\n\n\n                     Well done!\n")
	print("you have succeeded in your first hack. You have disabled an ")
	print("entire call tracking system and put them out of business.\n")
	print("Your next adventure will be even tougher.\n")
	print("Thanks for playing the game.\n")
	time.sleep(15)
	 
def end_screen():
	clear()
	print("Starting system shut down.")
	time.sleep(2)
	print("Flushing all numbers.")
	time.sleep(3)
	print("Flushing all encryption keys.")
	time.sleep(2)
	print("Resetting file system.")
	time.sleep(2)
	print("System shut down complete.")
	time.sleep(3)
	if (target_info[5]['tnumber']==""):
		win_screen()
	clear()	

# This returns raw input split by the first space found.
# format is opt1, opt2=split_input(raw_input("Enter input: "))
def split_input(entered):
	string1=""
	string2=""
	if entered.find(" ")==-1:
		string1=entered
	else:
		space_at=entered.find(" ")
		string1=entered[0:(space_at)]
		string2=entered[(space_at+1):len(entered)]
	return string1, string2

# This returns whether or not a file exists in local_files
# accepts file name
# returns ff as boleon and fn as file number
def file_to_check(ftc):
	ff=False
	for n, file_info in local_files.items():
		if (file_info['fname']==ftc):
			ff=True
			fn=n
	if ff==False:
		fn=0
	return ff, fn

#Record notes taken
def note_taken():
	print ("=== Note or number taken.===")
	
#Display Notes
def display_notes():
	print "Notebook version 2.2\n"
	if len(noted_numbers)==0:
		print "No numbers found yet."
	else:
		print ("Phone numbers found:\n")
		for n, note_info in noted_numbers.items():
			print (note_info['nnumber']+" "+note_info['nsource'])
	note_found=list.count(noted_keys,"        ")
	if note_found<8:
		print "\nNotes made.\n"
		for n in range(len(noted_keys)):
			if noted_keys[n]!="        ":
				print (noted_keys[n])
	else:
		print "\nNo notes made yet."

#Verifies correct crypto key
def check_for_key(kn, ki):
	kf=False
	if crypto_key[kn]==ki:
		kf=True
	return kf

#check for yes/no response
def check_yesno():
	yn="x"
	while yn !="y" and yn !="n":
		yn=raw_input("Initiate Payload? (y/n):")
		if yn=="y":
			answer=True
		if yn=="n":
			answer=False
	return answer	
		
#delivers end of game payload
def payload():
	print ("CRAY SYSTEM FOUND\n")
	initiate=check_yesno()
	if initiate==True:
		print ("\nInitiating payload...")
		time.sleep(2)
		print ("Searching for system registers...")
		time.sleep(4)
		hexkey="0123456789ABCDEF"
		for o in range(80):
			for p in range(15):
				hexpair=""
				for n in range(2):
					m=int(random.choice(range(0,16)))
					hexpair=hexpair+hexkey[m]
					print hexpair,
			print
			time.sleep(0.1)
		print ("\nDeleting...")
		time.sleep(2);
		print ("Hunting down all communication ports...")
		time.sleep(4);
		print ("Encrypting all ports...")
		for n in range(70):
			for m in range(40): 
				ch=chr(int(random.choice(range(16,32))))
				print ch,
			time.sleep(0.1)
			print
		time.sleep(2);
		print ("Cleaning up and removing all traces...")
		time.sleep(4);
		print ("Removing phone access...");
		time.sleep(3);
		print ('                 uuuuuuu')
		time.sleep(0.1)
		print ('             uu$$$$$$$$$$$uu')
		time.sleep(0.1)
		print ('          uu$$$$$$$$$$$$$$$$$uu')
		time.sleep(0.1)
		print ('         u$$$$$$$$$$$$$$$$$$$$$u')
		time.sleep(0.1)
		print ('        u$$$$$$$$$$$$$$$$$$$$$$$u')
		time.sleep(0.1)
		print ('       u$$$$$$$$$$$$$$$$$$$$$$$$$u')
		time.sleep(0.1)
		print ('       u$$$$$$$$$$$$$$$$$$$$$$$$$u')
		time.sleep(0.1)
		print ('       u$$$$$$"   "$$$"   "$$$$$$u')
		time.sleep(0.1)
		print ('       "$$$$"      u$u       $$$$"')
		time.sleep(0.1)
		print ('        $$$u       u$u       u$$$')
		time.sleep(0.1)
		print ('        $$$u      u$$$u      u$$$')
		time.sleep(0.1)
		print ('         "$$$$uu$$$   $$$uu$$$$"')
		time.sleep(0.1)
		print ('          "$$$$$$$"   "$$$$$$$"')
		time.sleep(0.1)
		print ('            u$$$$$$$u$$$$$$$u')
		time.sleep(0.1)
		print ('             u$"$"$"$"$"$"$u')
		time.sleep(0.1)
		print ('  uuu        $$u$ $ $ $ $u$$       uuu')
		time.sleep(0.1)
		print (' u$$$$        $$$$$u$u$u$$$       u$$$$')
		time.sleep(0.1)
		print ('  $$$$$uu      "$$$$$$$$$"     uu$$$$$$')
		time.sleep(0.1)
		print ('u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$')
		time.sleep(0.1)
		print ('$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"')
		time.sleep(0.1)
		print (' """      ""$$$$$$$$$$$uu ""$"""')
		time.sleep(0.1)
		print ('           uuuu ""$$$$$$$$$$uuu')
		time.sleep(0.1)
		print ('  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$')
		time.sleep(0.1)
		print ('  $$$$$$$$$$""""           ""$$$$$$$$$$$"')
		time.sleep(0.1)
		print ('   "$$$$$"                      ""$$$$""')
		time.sleep(0.1)
		print ('     $$$"                         $$$$"')
		time.sleep(2)
		print ("\n\nDamage done - clear down and run\n")
		time.sleep(2)
	else:
		print ("\nAborting payload...")
		time.sleep(3)
	return initiate
	
#Lists

crypto_key=load_crypto_keys()
tar_key=load_crypto_keys()
noted_keys=["        ","        ","        ","        ","        ","        ","        ","        "]

#Dictionaries

local_files = load_local_info()			
phone_info = load_phone_numbers()
noted_numbers = {}

target_info = load_target_info()
filename='shelve.out'


# Here we go

intro_screen()
start_screen()
terminate=False
while (terminate==False):
	msg="Invalid or unknown command."
	opt1, opt2=split_input(raw_input("A:> "))
	
#cheat for debugging a heap of anomalies
#	if (opt1=="cheat"):
#		for n, tinfo in (target_info.items()):
#				print (n, tinfo['tnumber'],tinfo['tsystem'])
#		
#		for n in range(len(crypto_key)):
#			print n, crypto_key[n]
#		for n in range(len(tar_key)):
#			print n, tar_key[n]+'.TAR'
#		msg=""

#exit
	if (opt1=="exit" or opt1=="quit"):
		terminate=True
		msg=""
#clear screen
	if (opt1=="cls" or opt1=="clear"):
		clear()
		msg=""
#directory
	if (opt1=="dir" or opt1=="ls"):
		msg=""
		print ("Volume in drive A has no label.");
		print ("Volume serial number is 1643-0CD7\n");
		print ("Directory of A:\\\n");
		for n, file_info in local_files.items():
			print (file_info['fdate']+" "+file_info['fsize']+" bytes "+file_info['fname'] )
#save game
	if (opt1=="save"):
		my_shelf = shelve.open(filename,'n') # 'n' for new
		for key in dir():
			try:
				my_shelf[key] = globals()[key]
				print ('Saving: {0}'.format(key))
				time.sleep(0.1)
			except TypeError:
		#
        # __builtins__, my_shelf, and imported modules can not be shelved.
				print ("....saving registers")
		#		print('ERROR shelving: {0}'.format(key))
		my_shelf.close()
		msg="Progress saved"
#load game
	if (opt1=="load"):
		filename='shelve.out'
		my_shelf = shelve.open(filename)
		for key in my_shelf:
			globals()[key]=my_shelf[key]
			print ('Restoriing: {0}'.format(key))
			time.sleep(0.1)
		my_shelf.close()
		msg="Progress restored"

#help
	if (opt1=="help" or opt1=="help.exe"):
		opt1="help.exe"
		filefound, filenumber = file_to_check(opt1)
		if filefound==True:
			clear()
			msg=""
			print ("Command Help version 2.11 (limited)\n")
			print ("Internal commands are:")
			print ("cls or clear    - clear screen")
			print ("dir or ls       - lists the contents of the current directory")
			print ("exit or quit    - shuts the system down")
			print ("type or cat     - display the contents of a file\n")
			print ("All commands and filenames are case sensitive.\n")
#Command
	if (opt1=="command" or opt1=="command.com"):
		opt1="command.com"
		filefound, filenumber = file_to_check(opt1)
		if filefound==True:
			msg=""
			print ("The Command Interpreter is already running.")
#notes
	if (opt1=="notes" or opt1=="notes.exe"):
		opt1="notes.exe"
		filefound, filenumber = file_to_check(opt1)
		if 	filefound==True:
			display_notes()
			msg=""
#zzmail			
	if (opt1=="zzmail" or opt1=="zzmail.exe"):
		opt1="zzmail.exe"
		filefound, filenumber = file_to_check(opt1)
		if 	filefound==True:
			clear()
			print ("ZZMAIL The quick and lazy message system\n")
        	print ("You have 2 messages.\n")
        	time.sleep(3)
        	print ("zzmail message 34255 received today from Martin B at 08:42\n")
        	print ("=SOM=")
        	print ("Sorry guys, but we need to do some system maintenance on the mail server. So, ")
        	print ("regretably it will be offline for most of today starting at 09:00 as well as")
        	print ("all of the weekend.")
        	print ("Apologies")
        	print ("Martin")
        	print ("Sys Admin")
        	print ("=EOM=\n")
        	time.sleep(3)
        	print ("zzmail message 34256 received today from Kevin M at 08:57\n")
        	print ("=SOM=")
        	print ("Shit! The message system is going down so I really hope you get this before ")
        	print ("Martin pulls the plug. I stumbled on a Wang VS system yesterday. There's an ")
        	print ("interesting document that might be worth checking out. Use the dialer to ")
        	print ("circumvent their security. Their access number is "+phone_info[0]["display_number"])
        	noted_numbers[0]={"nnumber": phone_info[0]["display_number"], "nsource":"Wang VS"}
        	print ("good luck")
        	print ("Kev.")
        	print ("=EOM=")
        	note_taken()
        	msg="zzmail complete."
#type view file contents
	if (opt1=="type" or opt1=="cat"):
		msg="No such File."
		filefound, filenumber = file_to_check(opt2)
		if (filefound==True):
#insert all the various files here
			typefile=opt2
			msg= ("= End of file =")
			print ("Contents of file "+typefile+"\n")
			if (typefile=="readme"):
				print ("Here's a few pointers to help you on your way.")
				print ("Find phone numbers to new systems, download any files")
				print ("you find and examine them for further clues. The NOTES")
				print ("program will keep track of any important information you")
				print ("uncover and is available at all times.")
				print ("\nYou can save your progress by using the save command and")
				print ("you can restore your saved point with the load command.") 
				print ("\nAlso, as a kindness, if you want to transfer all the")
				print ("files you find when using the dialer use the word all")
				print ("in conjuction with the t command")
				#print ("I have also enabled load and save so that you can backup your")
				#print ("progress as you go.\n")
				print ("Sys Admin")
			if (typefile=="0001.doc"): 
				print ("Annual Leave List for Accounts Department.")
				print ("==========================================\n")
				print ("Name               From        To            Contact Number")
				print ("Tony               May 14     May 21          "+phone_info[10]["display_number"])
				noted_numbers[10]={"nnumber": phone_info[10]["display_number"], "nsource":"Tony"}
				print ("Margaret           May 14     May 28          "+phone_info[11]["display_number"])
				noted_numbers[11]={"nnumber": phone_info[11]["display_number"], "nsource":"Margaret"}
				print ("Gerry              Jun 16     Jul  2          "+phone_info[12]["display_number"])
				noted_numbers[12]={"nnumber": phone_info[12]["display_number"], "nsource":"Gerry"}
				print ("Arnold             Jun 16     Jun 23          "+phone_info[13]["display_number"])
				noted_numbers[13]={"nnumber": phone_info[13]["display_number"], "nsource":"Arnold"}
				print ("Please ensure that this list is up to date at all times\n")
				print ("Brian Mastif")
				print ("Head of accounts")
				note_taken()
			if (typefile=="0002.doc"):
				print ("Margaret,")
				print ("What is the number for the printer repair people? The last engineer, Paul, ")
				print ("I think, gave me "+phone_info[1]["display_number"]+" but whenever I dial it I just get beeps ")
				noted_numbers[1]={"nnumber": phone_info[1]["display_number"], "nsource":"Digital"}
				print ("and screeches. The band printer is jammed AGAIN.")
				print ("regards")
				print ("Gerry")
				note_taken()
			if (typefile=="0003.doc"):
				print ("Notice to al staff.\n")
				print ("Please observe a strict numerical sequence when storing documents.")
				print ("Once again a document has been created that does not adhere to this standard.")
				print ("I appreciate that this is a new system to all of us, but let's not let it ")
				print ("degenerate into chaos.\n")
				print ("Would the author be so kind as to rectify this situation.\n")
				print ("Brian Mastif")
				print ("Head of accounts")
			if (typefile=="Personnel.LS"): 	
				print ("Name                  Dept           Ext             Pager")
				print ("----------------------------------------------------------")
				print ("David Rymer         Support          343             -")
				print ("Peter Alsop         Support          344             -")
				print ("Paul Franklin       Engineer         275             0324")
				print ("Sonia Keeler        Support          345             -")
				print ("Ahfar Djugo         Engineer         276             0434")
				print ("John Purfleet       Engineer         277             3434")
				print ("Frank Black         Consultant       104              -")
			if (typefile=="Proposal.TX"): 
				print ("Memo: Contract consultant")
				print ("To: Mary White - Personnel Dept.\n")
				print ("In light of the recent absences we are bringing in Frank Black from IBM for ")
				print ("3 months to help out in both support and engineering. Frank has worked with ")
				print ("us a number of times as is completely familiar with our products and ")
				print ("procedures. Please complete his terms of engagement and upload them to his ")
				print ("employers. Their system number is "+phone_info[2]["display_number"])
				noted_numbers[2]={"nnumber": phone_info[2]["display_number"], "nsource":"IBM"}
				print ("Richard Rymer")
				print ("DP Manager")
				note_taken()
			if (typefile=="Callouts.FX"):
				print (tar_key[7]+'.TAR')
				noted_keys[0]=tar_key[7]+'.TAR'
				note_taken()
			if (typefile=="Phone.LS"):
				hexkey="0123456789ABCDEF"
				for o in range(40):
					for p in range(20):
						hexpair=""
						for n in range(2):
							m=int(random.choice(range(0,16)))
							hexpair=hexpair+hexkey[m]
						print hexpair,
					print
			if (typefile=="Anomaly"):
				print ("Security concern.")
				print ("=================\n")
				print ("I have noticed a number of file dates out of sequence. While this is being ")
				print ("investigated please do not store any more files on our system. Please encrypt ")
				print ("and upload them to our file server over at TDC\n")
				print ("IT Management")
			if (typefile=="Telephones"):
				print ("Service                  Number")
				print ("------------------------------------\n")
				print ("Home access              "+phone_info[2]["display_number"])
				noted_numbers[2]={"nnumber": phone_info[2]["display_number"], "nsource":"IBM"}
				print ("File transfer            "+phone_info[4]["display_number"])
				noted_numbers[4]={"nnumber": phone_info[4]["display_number"], "nsource":"TDC"}
				print ("Bank transfers           "+phone_info[14]["display_number"])
				noted_numbers[14]={"nnumber": phone_info[14]["display_number"], "nsource":"Bank"}
				print ("IT Support tickets       "+phone_info[15]["display_number"])
				noted_numbers[15]={"nnumber": phone_info[15]["display_number"], "nsource":"It Support"}
				print ("Printer Faults           "+phone_info[16]["display_number"])
				noted_numbers[16]={"nnumber": phone_info[16]["display_number"], "nsource":"Faults"}
				note_taken()
			if (typefile=="pointer.doc"):
				print ("I have gotten a little out of my depth. Follow the printer and use "+crypto_key[5])
				noted_keys[1]=crypto_key[5]
				print ("KM")
				note_taken()
			if (typefile=="Pointer.TX"):
				key_valid=check_for_key(5, raw_input("Document encrypted, please supply key - "))
				if key_valid==True: 
					time.sleep(2)
					print ("To whoever finds this,")
					print ("There is an organisation out there that is acively harvesting all the phone ")
					print ("calls and electronic messages currently being transmitted. They must be ")
					print ("running on a huge computer like and IBM 370 or even a Cray.")
					print ("I think they detected my last log in attempt so I'm staying low.")
					print ("I also think one of the DEC consultants has a way into their system. He'll ")
					print ("leave the key you need scattered but in plain sight.")
					print ("KM")

				else: 
					print ("Invalid key. File closed.")
			if (typefile=="MissBlack.ac"): 
				print ("\n\n)")
				print ("                                        .,,, ,,,,, .")
				time.sleep(0.1)
				print ("                                   .AMMMMMMMMMMMMMMMM..")
				time.sleep(0.1)
				print ("                                 .:MMMHHMMMMMMMMMMMMMMMMA.")
				time.sleep(0.1)
				print ("                               .AMMMMHHHHMMMMMMMMHMMMMMMMMA:.")
				time.sleep(0.1)
				print ("                             .AMMMMMHHHHIIHIMMIIIHIIHMMMMMMMA.")
				time.sleep(0.1)
				print ("                           .AMMHMMMMHHHMMMMMIIMMMHMHIIHHMMMMMA.")
				time.sleep(0.1)
				print ("                          .AMHHMMMMHMMMMMMMMIMMMMMMMMMHHHMMMMMM.")
				time.sleep(0.1)
				print ("                         .AMHMMMMHHHMMMMMMMMHMMMMMMMMMMMHHMMMMMM:.")
				time.sleep(0.1)
				print ("                       .:AMHMMMMHHMMMMMMMMMMMMMMMMMMMMMMHHMMMMMMA..")
				time.sleep(0.1)
				print ("                       .MMMMMHHHMHHMMMMMMMMMMMMMMMMMMMMHHHHMMMMMMA..")
				time.sleep(0.1)
				print ("                     .:MMMHHHHHHHHHMMMMMMMMMMMMMMMMMMMMMIHHMMMMMMM:.")
				time.sleep(0.1)
				print ("                    ..MMMMHHHMHHHHHMMMMMMMMMMMMMMMHMMMMMHIHHMMMMMMMA.")
				time.sleep(0.1)
				print ("                    .AMMMMHMMHHIHHHMHMMMMMMMMMMMHHMMMMMMHIIHMMMMMMMM:.")
				time.sleep(0.1)
				print ("                   .MMMMMMMMMHHIIHHHMMMMMMMMMMMHIHHHMMHHHHIHMMMMMMMM")
				time.sleep(0.1)
				print ("                  .MHMMMMHMMMMHHIHIHIHMMMHMHMMHHHIHHIHHHHHHMMMMMMMMMM")
				time.sleep(0.1)
				print ("                  .AMMMMHMMMMMHIHHIHIIIIHIHIHHHIIHHIHHIHHMMMMMMMMMMMMM.")
				time.sleep(0.1)
				print ("                 .AMMMMMMMMMMMMMMHHHHIHIIHHIHHIIHHHIHHHMMMMMMMMMMMMMMM.")
				time.sleep(0.1)
				print ("                .MMMMMMMMMMMMMMMMMHHHHIHIHIHHIHHHHHHMMMMMMMMMMMMMMMMM")
				time.sleep(0.1)
				print ("                .AMMMMMMMMMMMMMMMHMMHMHHHHMMMMMMMHHMMMMMMMMMMMMMMMMMMMM.")
				time.sleep(0.1)
				print ("                MMMMMMMMMMMMV:IIMMMHMMMMHMMMMMMM:IHHMMMMMMMMMMMMMMMMMM")
				time.sleep(0.1)
				print ("               .AMMMMMMMMMMMV:I:MMMHIHMV:IMMMMMMI::I:MMMMMMMMMMMMMMMMMM.")
				time.sleep(0.1)
				print ("              .MMMMMMMMMMMM:.V:VMMIHMMI::MMMMMM::I:IMMMMMMMMMMMMMMMMMMM")
				time.sleep(0.1)
				print ("              .:MMMMMMMMMMMV,L,'.VHIIH:::VMMMMMA:I:HMMMMMMMMMMMMMMMMMMH.")
				time.sleep(0.1)
				print ("               AMMMMMMMMMMM::.'TMMA.:TTT:::VHHHMMHI:VMMMMMMMMMMMMMMMMMH:")
				time.sleep(0.1)
				print ("              .HMMMMMMMMMMV..,AAMMATPI..::::,:LLLIHHHMIMMMMMMMMMMMMMMMHH.")
				time.sleep(0.1)
				print ("              :HMMMMMMMMMM:.,:T:VMMBA:,:.:.:,:PHMMK:..T.HIMMMMMMMMMMMMMI")
				time.sleep(0.1)
				print ("             .:HMMMMMMMMMM:. .:I,PP,:AI:..:::AP'BMMHHA::I:MMMMMMMMMMMMMH")
				time.sleep(0.1)
				print ("             .HMMMMMMMMMMMI:...::::.:I. .::V:,'P':H:::::MMMMMMMMMMMMMI")
				time.sleep(0.1)
				print ("             ::MMMMMMMMMMMI:::. .:. .:I:. ::I..IIIII:..::IAMMMMMMMMMMMM")
				time.sleep(0.1)
				print ("             .:MMMMMMMMMMMM:.:... ..:I:. .:II. .:T:.:.::IAMMMMMMMMMMMMH.")
				time.sleep(0.1)
				print ("             .IMMMMMMMMMMMM:::.:. .:I:.. .:II:.. . .::::IMMMMMMMMMMMMMH.")
				time.sleep(0.1)
				print ("              .HMMMMMMMMMMM::::.:..I.::. .:III::...::::IHMMMMMMMMMMMMHI")
				time.sleep(0.1)
				print ("            .:IHMMMMMMMMMMMI:::::..:VA:.:.L:I::.:.:::IIAMMMMMMMMMMMHI.")
				time.sleep(0.1)
				print ("         .:I:.HIMMMMMMMMMMMI:::::....::T:HPP:..::.:::IIAMMMMMMMMMMMMI:")
				time.sleep(0.1)
				print ("    .: .:IH:H:HIMMMMMMMMMMMA:::::I:.,,:::.::.:.:.:::IIAMMMMMMMMMMMMH.")
				time.sleep(0.1)
				print ("     H.HIHMIMIAMMMMMMMMMMMMMA::::TPLIIIVVHIL,:II::::IIAMMMMMMMMMMMV.")
				time.sleep(0.1)
				print ("     MIMHMMIHMHMMMMMMMMMMMMMVL::::::TL:TTTPPPPT::I:IIAMMMMMMMMMMMV.   .")
				time.sleep(0.1)
				print ("     VMMHMMHMMMMHMHHMMMHMMMMI:L:::.:ITHHHTP:..::IIIAMMMMMMMMMMMMV HA. .:,")
				time.sleep(0.1)
				print ("      VMMMMMMMMHHIIHHHMMMMMI:.IL:::::IITHI::.::IIIAMMMMMMMMMMMMM..AMH AHM")
				time.sleep(0.1)
				print ("       ''VMMMMMMHHHHIMMHMMM::.::IL::.. . ..:::IIAH'VMMMMMMMMMMMMVMMMV.AMM")
				time.sleep(0.1)
				print ("          'VMMMMMMMMMMHHHHI:.:..:IHI::.:.:.:::AMHH  'VMMMMMMMMMMMMMMVMMMM")
				time.sleep(0.1)
				print ("                .AHHPI:::I:::...:::ITHLLLLLHMMMHHHI.   'VMMMHMMMMMMMMMMMV")
				time.sleep(0.1)
				print ("              .':TPT:.:.::.::..:::::::VHMMMMMHHIHIHHA.   'VMMHMMMMMMMMMV'")
				time.sleep(0.1)
				print ("           .-'...:... .. ......:.::::::IHMHIHIHIHIHIIHA:.  'VHHMMMMMMMH.")
				time.sleep(0.1)
				print ("         .'...:.. .. ..  . ....::.:.::::IIIII:::::.:.IHHHHA. 'VMMMHMHMV'")
				time.sleep(0.1)
				print ("       .' . .:.. . .  .  .  ....::.::::::::::::..:.::.IHMMMMMA. ''''''")
				time.sleep(0.1)
				print ("    .-' . . .. :  .  .. .   . ..:.:.::::.:..:::..:.:.:IIHHMMMMMMA.")
				time.sleep(0.1)
				print (" .-' ... .. ..: .:. ::..... .......:.::.:..:::.::.::::IIHHMMMMMMMMMA.")
				time.sleep(0.1)
				print ("' ..... .... ... ...:.::...:.. .. ....:.:..::::.:::::IIIIHHMMMMMMMMMMA.")
				time.sleep(0.1)
				print (". ........ ....:... .. . .  .. .. ..::..:.:..:.::::.::IIIHHMMMMMMMMMHHHI")
				print (".. ....... ......:.....::.::..::.:..:..:.:....:::...:::IIIIHHMMMMMHHHHHH.")
				time.sleep(0.1)
				print (". .... .... .. .....  .... .....:..:....:....:.:....::.:IIIIIHHMMHHHIHHH.")
				time.sleep(0.1)
				print (".. . ...:..:..:::..:.....::::...:.:..::.::..:..::..:.:.:::I:IIIHIHHIIHHH:")
				time.sleep(0.1)
				print (" . .. ......::.... ..... ...........:.:.:.:.:..::..::.:.:::IIIIIIHHIHHHH:")
				time.sleep(0.1)
				print (".......:.:..:::.... ... ..:.:.... ....:..:.:.:...:.::::.::::IIIIIIHHHHHH.")
				time.sleep(0.1)
				print ("..:.:.:.:.:... .. ... .. ..:.:......:..:.::.:....:.:::::.:::::IIIIHHHHHH.")
				time.sleep(0.1)
				print (":..:..::..:... . ... .. ..:...:.:.:.:::.:::..:...::::..::.:::::IIIIIHHHV")
				time.sleep(0.1)
				print (":.:..:.:..:.... ... .. ...::...:.:..:.:::.::...:.::::..:..:.:::IIIIIHHHI")
				time.sleep(0.1)
				print (".:..::.:.... .. ..  .. ....:..:...:...::::.::.:..:::.:..:..:.::IIIIHHHH:")
				time.sleep(0.1)
				print ("::.:.:.::.. .. ... ... ...:....:..:..:::.::..::..:.:...:...:::::IIIHHHV'")
				time.sleep(0.1)
				print (".::.::.:.... .. .. .. .. ... ....:..:::.::.:.:.::.:...:..:.::::::IHHHHI")
				time.sleep(0.1)
				print (":.:..:::.:.:..:. ... ... . ... ....:.:::.:..:.:.:.:..:..:..:::::AAHIHH:")
				time.sleep(0.1)
				print ("::.:.II:::...:..:.... .. .. .... .:..:::.::... ..:..:...:...::::MMIIHV'")
				time.sleep(0.1)
				print (":::IHHI::::I::.. ... .. . .. ....:.::::::.:.. .. .... .....:.:::MMIMHI")
				time.sleep(0.1)
				print (":IHHMMHIIHI:::... .. . ..  .. ....:.::::::.:.. ... ....:..:.::::IHIMH:")
				time.sleep(0.1)
				print ("IIHHMMMHMII:::.. .. .  . .. ... ..:..:::::.:... ... ....:.::.:::.VIMH.")
				time.sleep(0.1)
				print ("IIIHMMMMMHI::.. ...  ..  ... ..:..:..::I::.... .. ... ..:.:.::.::.VHH")
				time.sleep(0.1)
				print ("IHHVHMMHIII:::.. .. ... .. ... .:.::.::II::... . . .. ...:.:.:::::.VH")
				time.sleep(0.1)
				print ("IHW WMHHIII:::... .. ... .. ...:.:.:.::II::.:.. .. . .. ...:.:.:::I:H")
				time.sleep(0.1)
				print ("HH' :HHHHIII::.. .. . .,,,. .. .:. ..::II::.. .. . . .. ...:.:.:::I:H")
				time.sleep(0.1)
				print ("HV   VHHAIII::. .. ..:IIIIIA:...:..:::IIHI::... . . .. ...:.:.:.:IHHA.")
				time.sleep(0.1)
				print ("V    IHHHAI::.. ...:IIIIHAIHH::.::.::IIHIHI::..... .. ...:.::.:.:HI:MB")
				time.sleep(0.1)
				print ("     'HHHHAII:.. ..:II:IVIMHHI::.:.::IHHIIHII:::... ...:..:.:::.IHHMMM")
				time.sleep(0.1)
				print ("      VHHHH.:II:..::IHIIHMHHVI:.:.::IIHHIIIIHII:::...:..:.::.::.:HMMM'")
				time.sleep(0.1)
				print ("      IHHHHA.:II::.::VIHHMMVI::..::IIHMIIIIIIAII::::..:.:.::.::::VMMV")
				time.sleep(0.1)
				print ("      :HHHHHA.:III::::IHHHVI::::IIIIHMHIIIIIIIAHIII:::.:.:.:::IIIHV:H")
				time.sleep(0.1)
				print ("       VHHHHHHA:II:I::I:II::IIIHIIHVMHIIIIIIIIIIAHIIII:::::IIIHHI:AHH")
				time.sleep(0.1)
				print ("       IHHHHHHHHA::IIIIIIIIIIIIHIHVMHIIIIHIIIIIIIHMAIIIIIIIIIIV:MMHHH")
				time.sleep(0.1)
				print ("       IHHHHHHHHHMMIIIIIIIIIHIHIVMMHIIIIHIIIIII:IIVHMMMHHHH:HMMMHHHHH")
				time.sleep(0.1)
				print ("       :HHHHHHHHHHHMMMMMVHHHVMMMMHI:IIIIHHIIIII:::IVHMMHHHI:HMMMMHHHH")
				time.sleep(0.1)
				print ("        VHHHHHHHHHHHHMMMMMMMMMMHII:::IIIIHIIII:::::::VHMHH:IHMMMMHHHH.")
				time.sleep(0.1)
				print ("        IHHHHHHHHIHIHIHHHMHHHMIII:::::IIIHIII:::::IIIIVHHH:IHMMMMHHHHI")
				time.sleep(0.1)
				print ("        IHHHHHHHHHIHIHIIHHHIIIIIII::::IIIIIIII:::IIIIIIHHI:IHHMMHHHHHH.")
				time.sleep(0.1)
				print ("        IHHHHHHHHHHHIHIIHIIIIIII:::::::IIIIIII:::IIIIIIVH:IHHHHMHHHHHHI")
				time.sleep(0.1)
				print ("        IHHHHHHHHHHHHHIHIHIIIII:::::IIIIIIIIIII::IIIIIIIH:IHHHHHHHHHHHH.")
				time.sleep(0.1)
				print ("       .IHHHHHHHHHHHHHHHHHHHIIIIII::::IIIIIIII::IIIIIHHHH:II:IHHHHHHHHHI")
				time.sleep(0.1)
				print ("       HHHHHHHHHHHHHHHHHHIIIIIIIIIIIIIIIIIIIIIIIHIHHHMMM:I::IIHHIHHHHHH")
				time.sleep(0.1)
				print ("       AHHHHHHHHHHHHHHHHHHHIIIIIIIIIIIIIIIIIIIIIHIHHHMHMM.:.:IIHHIIHHHHH")
				time.sleep(0.1)
				print ("      AHHHHHHHHHHHIHIHIHIHIHIIIIIIIIIIIIHIHIHHIHIHHHHHMMM.:::IIIHHHHHHHM")
				time.sleep(0.1)
				print ("     AHHHHHHHHHHIHIHIIIHIHHIIIIIIIIIIIIHIHIHIHIHHHHHHMHMMI::IIIIIHIHHHHM.")
				time.sleep(0.1)
				print ("    AHHHHHHHIHIHIIIIIHIIHIIIIIIIIIIIIHIHIHIHHIHHHHHHHHHMMM:IIIIIIIIIHIHM.")
				time.sleep(0.1)
				print ("   AHHHHHHHIHIIIIIHIIIIHIIIIIIIIHIHIHIHHHHHHHIHIHIHHHHHHMM:IIIIIII:::IHM:")
				time.sleep(0.1)
				print ("  AHHHHHHHHHHIHIIIHIHIIHIHIHIIIIHIHHHHHHHMHHHIHIHIHIHHHHMM:IIIIII:::::IM:")
				time.sleep(0.1)
				print (" AHHHHHHHIHIHIIIHIIIIIIIHIIIHIIHIHIHHHHHMMHHHIHIHIHHHHHHMMI:IIIII:::::IM:")
				time.sleep(0.1)
				print ("AIHIHHHHHHIIHIIHIIIHIIIIHHIHIHIHIIHHHHIHMNI:HIHHIHHHHHHMMMIVHIII:::::IIMI")
				time.sleep(0.1)
				print ("HHHHHHHHHHHHHHIIIHIIIHIHIHIIHHIHHIHIHHIIMI:.:IIIHIHHHHMMMM IMHII:::::IIMI")
				time.sleep(0.1)
				print ("HHHHHHHHHHHIHIHIIIHIIIHIHIHIHIHHHIHIHHIHIHIIIIIIHIHHHHMMMM  VHII:::::IIM:")
				time.sleep(0.1)
				print ("HHHHHHHHHHHHIHIIIIIHIIIHIHIHIHIIIHIHIHIHHIIIIIHIHIIHHHMMMM  IHIII::::IHM:")
				time.sleep(0.1)
				print ("VHHHHHHHHHHHHHHIHIIIHIHIHIHIHIHIHIHIHIHIHIIIHIHHIHHHHMMMMM.  VHIII:::IHM.")
				time.sleep(0.1)
				print ("AIHHHHHHHHHHIHIIIHIIIHIHIHIHHIHIHHHIHIHIIIHIHHHHHHHHHMMMMM.  IHIII:::IHM")
				time.sleep(0.1)
				print ("HHIHHHIHIHIHIHIIIIIHIHIHIHIHIHIHIHIHIHIHIHIHIHHHHHHMMMMMMMI   VHHII:IIHM")
				time.sleep(0.1)
				print ("HMAIHIHIHIHIIHIIHIIHHIHHHIIIHHHIHIHIHIHIHHHIHIHHHHHHHMMMMMM   IHHIIIIHHM")
				time.sleep(0.1)
				print ("IHAIHIHIHIHIIIHIIIHIHIHHHIHHIHHIHHIHIHIHIHHHHHHIHHHHHMMMMMM.  'HHHIIIHHM")
				time.sleep(0.1)
				print ("IIHAIIHIHIIIHIIIHIHIHHIIHIHHIHHHHIHHHHIHHHIHHHHHHHHHHMMMMMMI   HHHIIIHHM.")
				time.sleep(0.1)
				print ("IIHHAIIHIIIIIIIIIHIHIHIIIHHHHIHHHIHHHHHHMMMMMHHHHMHMHMHHMPPH., HVIIIIHHM.")
				time.sleep(0.1)
				print ("IIIHHAIIHIIIIIHIHIHHIHHIHHHHIHHHHP''AHHPP'':'P:'''':'''    ...'VHIIIHHHM:")
				time.sleep(0.1)
				print (":IIIHHAIIIIHIHIHIHIHHHIHHIHHHHPL...:T......:.:.:.  ..... .... . 'VIIIHMMI")
				time.sleep(0.1)
				print (":::IIHAIIIIIIHIHIHIHHHIHHHHP::::II:...          ..... .... ........VIHMM'")
				time.sleep(0.1)
				print ("I::::IHAIHIIHHIHHHHHHPI::::::III::....:              ''''  .....:.:..VMV")
				time.sleep(0.1)
				print ("II::::IHAIHHHHHHHHPP:::::IIIIII':..     ..  ...    ...     ..:.:..::..V)")
				time.sleep(0.1)
				print ("III::::IIAHHHHHP:::::::IHHHH'...  .. ..  ..  ..  ......  .  .:HA..I...'")
				time.sleep(0.1)
				print ("IIII::::IIIAHV:::::::IIIVMM..... ..PPMMMH. .A.. ........ .:...IHH.::'")
				time.sleep(0.1)
				print ("IIIIII::::::::::::::::IIHIV.....::::HMMMMM..M...........A..H...MMV'")
				time.sleep(0.1)
				print ("IIIIII::::::::::::::II::::.....::::AHMMMMMMIIHMMMLL......H..HH.MV'")
				time.sleep(0.1)
				print ("A:IIIIII:::::::::IIIIIIIII::::::I:AHHMHMMHMIIMMMHHHHHHHHHHMMMMMM'")
				time.sleep(0.1)
				print ("HA:IIIIIIIII::::IIIIIIIIIII:::IIAHMIMMMMMMMMMMMMMMMHMMHMMHMMMMMI")
				time.sleep(0.1)
				print ("HHA::IIIIIIIIIIIIIIIIIIIIIIIIIIAHM:HMHMMMMMMMMMMHMMMIHHMMMMHIH:A.")
				time.sleep(0.1)
				print ("HHIA::IIIIIIIIIIHIHIHIHIHIHIIHHIM:HH:IHHHHHHIIHHHMMIHHHMIHMIH:MMA")
				time.sleep(0.1)
				print ("HHHIIAA::IIIIHIHIHHHIHIHIHIHIIHIII:IHHHHHMMI:IHHMHIHHMIIHMIHVHMMM.")
				time.sleep(0.1)
				print ("HHHHII:HHHHHLLLLIHIHHIHIHHI:HHHIIIHHA::VHV:::IHV::IHVI:IV::I:HMMMA")
				time.sleep(0.1)
				print ("IHHHIII:HHMMMMMMMMMMMMHIIIIIIAIIIIII:''')::IHMV::IHV::IV::I:HHHMMM.")
				time.sleep(0.1)
				print ("IIIHHHII:HHHMMMMMMMMMM:MMMMM::TTTTTT::::::IHV:::IHV::IV::I:HHHHMMMA")
				time.sleep(0.1)
				print ("IIIIIHIIII:HMMMMMMMMMM:HMHHHII.:::...::I:'IV:::IVP::IV.:IVIIHHHHHMM.")
				time.sleep(0.1)
				print ("IIIIIIIIIIII:HMMMMMMMM:..IHI...::.....:: .V.::IVP::IV::'VIIIHHHHHHHA")
				time.sleep(0.1)
				print ("IIIIIIIIIIIII:IHHHHMM..........::.....::.V.:IIVP::IVHI .AIIIIHHHHHHM.")
				time.sleep(0.1)
				print ("IIIIIIIHIIIIIIIIIIHHM..........:.......::I:'IAP:-'I:.:LAIIIIIHHHHHHMA")
				time.sleep(0.1)
				print ("IIIIIHIIIIIIIIIIIHIHM ....:... :.....:..:I .AP:' ,A:..IIIIIIIIHHHHHMM.")
				time.sleep(0.1)
				print ("IIIHIIHIIIIIIIIIIIIII....:.....:.....:...:T:::: A::...IIIIIIIIHHHHHMMA")
				time.sleep(0.1)
				print ("IIIIHIIIIIIIIIIIIIII...:.......:.....:........:T:.....IIIIIIIIHHHHHHMM.")
				time.sleep(0.1)
				print ("IIIIIIIIIIIIIIIIIIII...........:.....:........:.......IIIIIIIHHHHHHHMMA")
				time.sleep(0.1)
				print ("IIIHIIIIIIIIIIIIHIHI...........:.....:........:..:....IIIIIIIIHIHHHMHMM")
				time.sleep(0.1)
				print ("IHIIIIIIIIIIIIIHIHI............:.....:.......::..:...IIIIIIIIHIHHHHMHMM.")
				time.sleep(0.1)
				print ("IIIIIIIIIIIIIIIHIHI.............:....::......::..:...IIIIIIIIIHIHMHMHMMI")
				time.sleep(0.1)
				print ("IIIIIIIIIIIIIIIIHIH............::....::......::..:...IIIIIIIIIHIHHMHMHMM")
				time.sleep(0.1)
				print ("HIIIIIIIIIIIIIIIHI.............::....::......::.::...IIIIIIIIIHHIHHMHHMM.")
				time.sleep(0.1)
				print ("HHIIIIIIIIIIIIIIHH.............::....::......::.::....IIIIIIIIIIIHIHIHMHI")
				time.sleep(0.1)
				print ("HHHIIIIIIIIIIIIIHI.............::...:::.....:::.::....HIIIIIIIIIHHIHIHMMM")
				time.sleep(0.1)
				print ("VHHHIIIIIIIIIIIHI..............:....:::......::.::....HHIIIIIIIIIIIIHIHMM")
				time.sleep(0.1)
				print ("'HHHHIIIIIIIIIIIH.............:::....::.....:...::....HHHIIIIIIIIIIIIHHMM")
				time.sleep(0.1)
				print (" VHHHHHIIIIIIIIIH.............::::...:.::...::...:....HHHIIIIIIIIHIHIHHMM")
				time.sleep(0.1)
				print ("  VHHHHHHHIIIHHH..............:::....:.::...::...:....HHHHHHIIIIIIHIHHHMM")
				time.sleep(0.1)
				print ("")
				time.sleep(0.1)
				print ("                  MISS 'BLACK IS BEAUTIFUL' PLAYMATE")
				time.sleep(0.1)
				print ("                            OCTOBER 1969")
				time.sleep(0.1)
				print ("       ORIGINATED FOR RTTY BY DON, WA6PIR, ENCINO, CALIFORNIA")
			if (typefile=="Staff"): 
				print ("Memo regarding current contract staff")
				print ("------------------------------------------------------\n")
				print ("Please be aware that Frank Black is on secondment to Digital and will delegate ")
				print ("his Honeywell duties to Samantha. His email will continue to route via ")
				print ("Honeywell.")
			if (typefile=="Enquiries"): 
				print ("Sam,")
				print ("Would you be a sweetie and monitor my mail in Honeywell while I'm over at ")
				print ("Digital? Their access number is "+phone_info[3]["display_number"])
				noted_numbers[3]={"nnumber": phone_info[3]["display_number"], "nsource":"Honeywell"}
				print ("It's only for a week or two. Passwords are the same as for here.")
				print ("Frank")
				note_taken()
			if (typefile=="0002548.msg"):
				print ("From: John Small")
				print ("To: George Gibbins")
				print ("Subject: Lavatories")
				print ("===================")
				print ("The state of our facilties is deplorable. God forbid that a customer ever has ")
				print ("to use them. Please admonish our janitor and ensure that the night cleaning ")
				print ("staff pay better attention\n")
				print ("Office Manager")
			if (typefile=="0003674.msg"):
				print ("From: Joyce Poppeti")
				print ("To: Gerry Davisdon")
				print ("Subject: Contract Staff")
				print ("=======================")
				print ("Gerry,")
				print ("Please ensure that all contract staff leave their messages on their native ")
				print ("systems instead of cluttering ours up and then leaving them there forever.")
				print ("Joyce")
			if (typefile=="0008467.msg"): 
				print ("From: Maureen Tredgold")
				print ("To: Frank Black")
				print ("Subject: Where are you?")
				print ("=======================")
				print ("Hey Frankie,")
				print ("When are going to visit us again? Fancy lunch next time?")
				print ("Mo")
			if (typefile=="0010005.msg"): 
				print ("From: KevinM@Jebred.az")
				print ("To: Frank Black")
				print ("Subject: Assistance")
				print ("===================")
				print ("Frank, would you do me a big favour and upload that neat little program to ")
				print ("our usual drop point. I have to keep this a bit hush hush and will explain ")
				print ("when we meet later.")
				print ("Many thanks - Kev")
			if (typefile=="0010006.msg"):
				partkey="        "
				temp_partkey=crypto_key[7][0:2]+partkey[2:4]+partkey[4:6]+partkey[6:8]
				partkey=temp_partkey
				temp_partkey=crypto_key[7][0:2]+noted_keys[7][2:4]+noted_keys[7][4:6]+noted_keys[7][6:8]
				noted_keys[7]=temp_partkey
				print ("From: Frank Black")
				print ("To: Sys OP 12")
				print ("Subject: Assistance "+partkey)
				print ("======================")
				print ("Paul - do me favour. I'm on secondment to DEC and cant get at our FTP server ")
				print ("over at TDC. Please encrypt the spike program using key "+crypto_key[3]+".")
				noted_keys[3]=crypto_key[3]
				print ("Let me have the filename in due course.\n")
				print ("Thanks")
				print ("Frank")
				note_taken()
			if (typefile=="0010007.msg"):
				print ("From: Sys OP 12")
				print ("To: Frank Black")
				print ("Subject: Assistance")
				print ("===================")
				print ("Hi Frank,")
				print ("How is life in the world of PDPs? Transfer done to file "+tar_key[3]+" using ")
				noted_keys[2]=tar_key[3]+'.TAR'
				print ("TAR compression.\n")
				print ("Have fun. - Paul")
				note_taken()
			if (typefile=="0012453.msg"):
				print ("From: Alan Brown")
				print ("To: Gerry Davidson")
				print ("Subject: Keys")
				print ("=============")
				print ("Gerry,")
				print ("I'm away for 4 weeks at our Montreal office. I have left the safe keys in my ")
				print ("top drawer. Please take them.")
				print ("Alan")
			if (typefile=="0012544.msg"):
				partkey="        "
				temp_partkey=partkey[0:2]+crypto_key[7][2:4]+partkey[4:6]+partkey[6:8]
				partkey=temp_partkey
				temp_partkey=noted_keys[7][0:2]+crypto_key[7][2:4]+noted_keys[7][4:6]+noted_keys[7][6:8]
				noted_keys[7]=temp_partkey
				print ("From: Frank Black")
				print ("To: KevinM@Jebred.az")
				print ("Subject: Assistance "+partkey)
				print ("=======================")
				print ("Hi Kev,")
				print ("You'll find it in the usual slot. "+tar_key[3]+".TAR\n")
				noted_keys[2]=tar_key[3]+".TAR"
				print ("Good luck")
				print ("Frank")
				note_taken()
			if (typefile=="0012555.msg"):
				print ("From: KevinM@Jebred.az")
				print ("To: Frank Black")
				print ("Subject: Assistance")
				print ("===================")
				print ("Frank,")
				print ("What exactly does it do?")
				print ("Kev")
			if (typefile=="0012556.msg"):
				partkey="        "
				temp_partkey=partkey[0:2]+partkey[2:4]+crypto_key[7][4:6]+partkey[6:8]
				partkey=temp_partkey
				temp_partkey=noted_keys[7][0:2]+noted_keys[7][2:4]+crypto_key[7][4:6]+noted_keys[7][6:8]
				noted_keys[7]=temp_partkey
				print ("From: Frank Black")
				print ("To: KevinM@Jebred.az")
				print ("Subject: Assistance "+partkey)
				print ("=======================")
				print ("Hi Kev,")
				print ("Be careful where you put this. It works at a kernel level and does it's damage ")
				print ("by finding and NULLing all the registers it can find. For network connected ")
				print ("devices it's the end of the line. It will NIX all connections irreversably. ")
				print ("Then it will drop them from the phone system forever.")
				print ("Good luck.")
				print ("Frank.")
				note_taken()
			if (typefile=="0012557.msg"):
				partkey="        "
				temp_partkey=partkey[0:2]+partkey[2:4]+partkey[4:6]+crypto_key[7][6:8]
				partkey=temp_partkey
				temp_partkey=noted_keys[7][0:2]+noted_keys[7][2:4]+noted_keys[7][4:6]+crypto_key[7][6:8]
				noted_keys[7]=temp_partkey
				print ("From: Frank Black")
				print ("To: KevinM@Jebred.az")
				print ("Subject: Assistance "+partkey)
				print ("=======================")
				print ("Hi Kev,")
				print ("Don't forget to clear down this thread.")
				print ("Frank.")
				note_taken()
			if (typefile==tar_key[3]+'.TAR'):
				key_valid=check_for_key(3, raw_input("Document encrypted, please supply key - "))
				if key_valid==True: 
					time.sleep(2)
					doption2="stinger.exe"
					filefound, filenumber = file_to_check(doption2)
					if(filefound==True):
						print "File already exists locally."
					else:
						next_record=len(local_files)
						local_files.update({next_record:{'fname':doption2, 
						'fsize':str(int(1+random.random()*98))+","+str(int(100+random.random()*898)), 
						'fdate':'24/08/88'}})
						print ("File "+doption2+" successfully decrypted")
				else:
					print ("Invalid key. File closed.")
			if (typefile==tar_key[0]+".TAR"):
				key_valid=check_for_key(0, raw_input("Document encrypted, please supply key - "))
				if key_valid==True:
					time.sleep(2)
					print ("There is no way you got this key without cheating.")
				else: 
					print ("Invalid key. File closed.")
			if (typefile==tar_key[2]+".TAR"):
				key_valid=check_for_key(2, raw_input("Document encrypted, please supply key - "))
				if key_valid==True:
					time.sleep(2)
					print ("There is no way you got this key without cheating.")
				else: 
					print ("Invalid key. File closed.")
			if (typefile==tar_key[4]+".TAR"):
				key_valid=check_for_key(4, raw_input("Document encrypted, please supply key - "))
				if key_valid==True:
					time.sleep(2)
					print ("There is no way you got this key without cheating.")
				else: 
					print ("Invalid key. File closed.")
			if (typefile==tar_key[7]+".TAR"):
				key_valid=check_for_key(7, raw_input("Document encrypted, please supply key - "))
				if key_valid==True:
					time.sleep(2)
					print ("One juicy crayfish waiting at "+phone_info[5]["display_number"])
					noted_numbers[5]={"nnumber": phone_info[5]["display_number"], "nsource":"Cray"}
					note_taken()
				else: 
					print ("Invalid key. File closed.")


		
		print			

#dialer
	if(opt1== "dialer" or opt1=="dialer.exe"):
		opt1='dialer.exe'
		filefound, filenumber =file_to_check(opt1)
		if filefound==True:
			clear()
			print ("Open Modem Dialer version 1.7\n")
			dialer=(raw_input("Number to dial, (n)otes or (e)xit - "))
			while(dialer!="e"):
				if(dialer=="n"): 
					display_notes()
				else:
					print ("\nOff hook, dialing "+dialer)
					number_found=False
					dialer_target=0
					for n, tinfo in target_info.items():
						if (tinfo['tnumber'])==dialer:
							number_found=True
							dialer_target=n 
					if(number_found == True):
						playsound('dial-up-modem-01.wav')						
						print ("Carrier detected, negotiating speed.")
						time.sleep(2)
						print ("Connect 2400 V.22bis")
						time.sleep(1)
						print ("Interrogating remote system\n")
						time.sleep(2)
						print ("Remote system is "+target_info[dialer_target]['tsystem'])
						doption1=""
						doption2=""
						while(doption1 != "d"): 
							dialermessage="Invalid option"
							doption1=raw_input("(l)ist, (t)ransfer, (d)isconnect - ")
							doption1, doption2 = split_input(doption1)
# disconnect
							if(doption1=="d"): 
								print ("Dropping line.")
								time.sleep(2)
								dialermessage="On hook. line disconnected."
# list files
							if(doption1=="l"): 
								dialermessage="File listing complete"
#*the cray and bank computers*
								if((dialer_target == 5) or (dialer_target == 7)):
									time.sleep(10)
									print ("Cannot access file system. 2048 bit encryption encountered.")
								else:
									print ("Searching for accessible files, please wait...")
									nofiles=len(target_info[dialer_target]['tfiles'])
									if nofiles!=0:
										for tfile in (target_info[dialer_target]['tfiles']):
											time.sleep(2)
											print tfile
									else:
										print ("No files found.")
# transfer file											
							if(doption1=="t"): 
								if(doption2==""):
									print("File name missing.") 
								else :
									if (doption2=="all"):
										if (len(target_info[dialer_target]['tfiles'])>0):
											for tfile in (target_info[dialer_target]['tfiles']):
												time.sleep(2)
												next_record=len(local_files)
												doption2=tfile
												filefound, filenumber = file_to_check(doption2)
												if(filefound==True):
													print("File "+doption2+" already exists locally.")
												else:
													local_files.update({next_record:{'fname':tfile, 
													'fsize':str(int(1+random.random()*98))+","+str(int(100+random.random()*898)), 
													'fdate':'24/08/88'}})
													print("File "+doption2+" successfully transferred")
										else:
											print ("No files available for transfer")
									else:
										filefound=list.count(target_info[dialer_target]['tfiles'], doption2)
										if(filefound == 0):
											print("Invalid file name.")
										else:
											filefound, filenumber = file_to_check(doption2)
											if(filefound==True):
												print("File "+doption2+" already exists locally.")
											else:
												next_record=len(local_files)
												local_files.update({next_record:{'fname':doption2, 
												'fsize':str(int(1+random.random()*98))+","+str(int(100+random.random()*898)), 
												'fdate':'24/08/88'}})
												time.sleep(2)
												print("File "+doption2+" successfully transferred")
					else:
						playsound('modem-dialing-01.wav')
						time.sleep(2)
						playsound('Wrong-number.mp3')
						playsound('Wrong-number.mp3') 
						print ("No carrier detected.")
						time.sleep(2)
						print ("Invalid number, no modem detected.")
				dialer=(raw_input("Number to dial, (n)otes or (e)xit - "))
		msg=("Dialer complete.")
# stinger
	if((opt1=="stinger") or (opt1=="stinger.exe")): 
		opt1="stinger.exe"
		filefound, filenumber = file_to_check(opt1)
		if filefound==True:
			msg=""
			clear()
			print ("STINGER version 2.45\n")
			dialer=""
			while(dialer!="e"):
				dialer=(raw_input("Number to dial, (n)otes or (e)xit - "))
				if(dialer=="n"): 
					display_notes()
				else:
					if(dialer!="e"):
						print ("\nOff hook, dialing "+dialer)
						number_found=False
						dialer_target=0
						for n, tinfo in target_info.items():
							if (tinfo['tnumber'])==dialer:
								number_found=True
								dialer_target=n 
						if(number_found == True):
							playsound('dial-up-modem-01.wav')						
							print ("Carrier detected, negotiating speed.")
							time.sleep(2)
							print ("Connect 9600 V.32")
							time.sleep(1)
							print ("Probing remote system\n")
							time.sleep(7)
							if dialer_target!=5:
								print ("Incompatible Operating System.")
								time.sleep(3)
								print ("Aborting Stinger!")
							else:
								initiate=payload()
								if initiate==True:
									target_info[dialer_target]['tnumber']=""
									time.sleep(3);
									print("System offline!")
								else:
									time.sleep(3)
									print ("Aborting Stinger!")
						else :
							playsound('modem-dialing-01.wav') 
							time.sleep(2)
							playsound('Wrong-number.mp3')
							playsound('Wrong-number.mp3') 
							print ("No carrier detected.")
							time.sleep(2)
							print ("Invalid number, no modem detected.")
	print msg
end_screen()
