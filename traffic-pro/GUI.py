from logging import root
from tkinter import *
import tkinter.font
import hashlib as hlib
import tkinter.messagebox
from datetime import timedelta
import os
import hashlib
import binascii
import re
from tkinter import ttk
from datetime import datetime
import zlib,base64





def login_in():
	global id_input_login
	global password_input_login
	global login_menu

	login_menu=Tk()	
	login_menu.geometry('900x500+300+100')
	login_menu.resizable(1920,1080)
	login_menu.title("LOGIN MAIN")
	login_menu.configure(bg='#FFDEDE')
	login_menu = Canvas(login_menu,width = 900, height = 500)
	login_menu.pack()
	image = PhotoImage(file='bg2.png')
	login_menu.create_image(0,0,anchor = NW, image = image)

	k_font = tkinter.font.Font(family='Times New Roman', size=15, weight=tkinter.font.BOLD)
	id_label1=Label(login_menu,text="TRAFFIC VIOLATION MANAGEMENT", font="Times 30 italic bold",fg='black',bg='#B2C8DF',relief='solid',width=32)
	id_label1.place(x=85,y=50)

	id_label=Label(login_menu,text="Your ID", font="Times 20 italic bold",fg='#EAF6F6',bg='#FF0063')
	id_label.place(x=285,y=150)
	
	password_label=Label(login_menu,text="Password",font="Times 20 italic bold",fg='#EAF6F6',bg='#FF0063')
	password_label.place(x=270,y=200)

	id_input_login=Entry(login_menu,width=15,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
	id_input_login.place(x=450,y=155)
	
	password_input_login=Entry(login_menu,width=15,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
	password_input_login.place(x=450,y=205)

	loginbutton1=Button(login_menu,command=login_check,text=" LOGIN ",bg='light blue',height=1,width=12,font=k_font)
	loginbutton1.place(x=385,y=270)

	registerbutton=Button(login_menu,command=register_in,text=" REGISTER ",bg='light green',height=1,width=12,font=k_font)
	registerbutton.place(x=385,y=320)

	adminbutton=Button(login_menu,command=admin_in,text=" ADMIN LOGIN ",bg='light coral',height=1,width=12,font=k_font)
	adminbutton.place(x=385,y=370)
	password_input_login.config(show="*")

	login_menu.mainloop()

def login_check():
	global id
	global name
	id=id_input_login.get()
	password=password_input_login.get()

	pos = binary_search('UserIndex.txt', id)
	if pos == -1:
		tkinter.messagebox.showinfo("Login"," User ID is incorrect.Please reenter")
		return(login_in)
	else:
		f2 = open ('UserprofileWithHashing.txt', 'r')
		f2.seek(int(pos))
		l = f2.readline()
		l = l.rstrip()
		word = l.split('|')
		name=word[1]
		if(verify_password(word[3], password)):
			tkinter.messagebox.showinfo("Login","Login Successful!")
			login_menu.destroy()
			Main_Menu()
		else:
			tkinter.messagebox.showinfo("Login"," Password that you have entered is incorrect.Please reenter")
			return(login_in)
		f2.close()


def register_in():
	global id_input
	global name_input
	global email_input
	global password_input
	global register_menu

	register_menu=Tk()
	register_menu.wm_title("Register")
	register_menu.geometry('900x500+300+100')
	register_menu.minsize(900,500)
	register_menu.maxsize(900,500)
	register_menu.resizable(0,0)
	register_menu.configure(bg='#FF8B8B')
	# register_menu = Canvas(register_menu,width = 900, height = 500)
	# register_menu.pack()
	# image1 = PhotoImage(file='C:\\Users\\ullas\\Desktop\\traffic-pro\\images\\bg1.png')
	# register_menu.create_image(0,0,anchor = NW, image = image1)
	

	k_font = tkinter.font.Font(family='Montserrat', size=15, weight=tkinter.font.BOLD)


	sign_up=Label(register_menu,text="Let's Create Your Account", font="Times 30 italic bold",fg='black',bg='#B2C8DF',relief='solid',width=22)
	sign_up.place(x=200,y=30)

	id_label=Label(register_menu,text="Your ID",fg='#EAF6F6',bg='#FF0063',font="Times 20 italic bold")
	id_label.place(x=285,y=120)

	name_label=Label(register_menu,text="Full Name",fg='#EAF6F6',bg='#FF0063',font="Times 20 italic bold")
	name_label.place(x=255,y=180)

	email_label=Label(register_menu,text="Email",fg='#EAF6F6',bg='#FF0063',font="Times 20 italic bold")
	email_label.place(x=310,y=230)

	password_label=Label(register_menu,text="Password",fg='#EAF6F6',bg='#FF0063',font="Times 20 italic bold")
	password_label.place(x=270,y=280)

	id_input=Entry(register_menu,width=20,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
	id_input.place(x=450,y=135)

	name_input=Entry(register_menu,width=20,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
	name_input.place(x=450,y=185)

	email_input=Entry(register_menu,width=20,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
	email_input.place(x=450,y=235)

	password_input=Entry(register_menu,width=20,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
	password_input.place(x=450,y=285)

	loginbutton1=Button(register_menu,command=login_in,text=" L O G I N ",bg='light blue',height=2,width=15,font=k_font)
	loginbutton1.place(x=395,y=350)

	registerbutton=Button(register_menu,command=register_check,text=" R E G I S T E R ",bg='light grey',height=2,width=15,font=k_font)
	registerbutton.place(x=395,y=420)

	password_input.config(show="*")

	
	register_menu.mainloop()

def isValidEmail(str):
	regex = ("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$")
	p = re.compile(regex)
	if (str == None):
		return False
	if(re.search(p, str)):
		return True
	else:
		return False

def register_check():
	global id

	id=id_input.get()
	name=name_input.get()
	email=email_input.get()
	password=password_input.get()

	if len(id)<1 or id.isdigit()==False:
		tkinter.messagebox.showinfo("Enter ID","Please renter the details (ID should be atleast 1 positive integers)")
		register_menu.lift()
		return(register_in)

	if len(name)==0:
		tkinter.messagebox.showinfo("Enter Name","You did not type  name O_O")
		register_menu.lift()
		return(register_in)

	c=isValidEmail(email)
	
	if (c)==False:
		tkinter.messagebox.showinfo("Enter Email Address","You did not type an Email (abc@gmail.com) O_O")
		register_menu.lift()
		return(register_in)

	if len(password)==0 or len(password)<5  :
		tkinter.messagebox.showinfo("Enter Password","You did not type a Password (greater than 5 characters) O_O")
		register_menu.lift()
		return(register_in)

	pos = binary_search('UserIndex.txt',id)
	if pos != -1:
		tkinter.messagebox.showinfo("Register","Already registered. Choose a different ID")
		register_menu.destroy()

	f4= open('Userdata.txt','a+')
	f6=open('MainUserData.txt','a+')
	f7=open('MainUserProfileWithHashing.txt','a+')
	f5=open('MainUserIndex.txt','a+')
	f2 = open ('UserprofileWithHashing.txt', 'a+')
	pos = f2.tell()
	f3 = open ('UserIndex.txt', 'a+')
	buf = id + '|' + name + '|' + email + '|' + hash_password(password) + '|' + '$'
	f2.write(buf)
	f2.write('\n')
	buf = id + '|' + name + '|' + email + '|' + hash_password(password) + '$'
	f7.write(buf)
	f7.write('\n')
	buf = id + '|' + str(pos) + '|' + '$'
	f3.write(buf)
	f3.write('\n')
	buf = id + '|' + name +'|'+ email + '|' + password + '|' +'$'
	f4.write(buf)
	f4.write('\n')
	buf = id + '|' + name +'|'+ email + '|' + password  +'$'
	f6.write(buf)
	f6.write('\n')
	buf = id + '|' + str(pos) + '$'
	f5.write(buf)
	f5.write('\n')
	f5.close()
	f4.close()
	f3.close()
	f2.close()
	f7.close()
	f6.close()
	key_sort('UserIndex.txt')
	filecomp('Userdata.txt','CompressedUserData.txt')
	tkinter.messagebox.showinfo("Register","Registration Successful!")
	register_menu.destroy()


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def admin_in():
		global id_admin
		global password_admin
		global admin_menu

		admin_menu=Tk()
		admin_menu.wm_title("ADMIN LOGIN")
		admin_menu.geometry('900x500+300+100')
		admin_menu.minsize(900,500)
		admin_menu.maxsize(900,500)
		admin_menu.resizable(0,0)
		
		admin_menu.configure(bg='#FFDEDE')
		# admin_menu = Canvas(admin_menu,width = 900, height = 500)
		# admin_menu.pack()
		# image = PhotoImage(file='C:\\Users\\ullas\\Desktop\\traffic-pro\\images\\bg2.png')
		# admin_menu.create_image(0,0,anchor = NW, image = image)
		
		
		k_font = tkinter.font.Font(family='Times New Roman', size=15, weight=tkinter.font.BOLD)

		admin=Label(admin_menu,text="ADMIN LOGIN", font="Times 30 italic bold",fg='black',bg='#B2C8DF',relief='solid',width=15)
		admin.place(x=280,y=30)

		admin_label=Label(admin_menu,text="ADMIN ID",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
		admin_label.place(x=288,y=150)

		admin_password_label=Label(admin_menu,text="PASSWORD",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
		admin_password_label.place(x=270,y=225)

		id_admin=Entry(admin_menu,width=15,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
		id_admin.place(x=450,y=155)

		password_admin=Entry(admin_menu,width=15,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
		password_admin.place(x=450,y=230)

		loginbutton2=Button(admin_menu,command=admin_check,text=" L O G I N ",bg='light blue',height=2,width=10,font=k_font)
		loginbutton2.place(x=395,y=320)
		password_admin.config(show="*")

		admin_menu.mainloop()

def admin_check():
	global admin_id

	admin_id=id_admin.get()
	admin_password=password_admin.get()

	if admin_id=="admin" and admin_password=="admin":
		tkinter.messagebox.showinfo("Login","Admin Login Successful!")
		admin_menu.destroy()
		login_menu.destroy()
		Admin_Opt()
	else:
		tkinter.messagebox.showinfo("Login","Admin id or password INCORRECT. Please reenter")

def Admin_Opt():
		global opt_menu

		opt_menu=Tk()
		opt_menu.wm_title("ADMIN MENU")
		opt_menu.geometry('900x500+300+100')
		opt_menu.minsize(900,500)
		opt_menu.maxsize(900,500)
		opt_menu.resizable(0,0)
		opt_menu.configure(bg='#FFDEDE')
		# opt_menu = Canvas(opt_menu,width = 900, height = 500)
		# opt_menu.pack()
		# image = PhotoImage(file='C:\\Users\\ullas\\Desktop\\traffic-pro\\images\\bg2.png')
		# opt_menu.create_image(0,0,anchor = NW, image = image)

		k_font = tkinter.font.Font(family='Times new roman', size=15, weight=tkinter.font.BOLD)

		opt=Label(opt_menu,text="ADMIN OPTIONS", font="Times 30 italic bold",fg='black',bg='#B2C8DF',relief='solid',width=15)
		opt.place(x=290,y=30)

		addbutton=Button(opt_menu,command=add_case,text=" ADD NEW CASE ",bg='#FF8B8B',height=2,width=15,font=k_font)
		addbutton.place(x=400,y=150)

		delbutton=Button(opt_menu,command=del_case,text=" DELETE CASE ",bg='#FF8B8B',fg='white',height=2,width=15,font=k_font)
		delbutton.place(x=400,y=250)

		backbutton=Button(opt_menu,command=reopen_login,text=" LOG OUT ",bg='red',height=2,width=15,font=k_font)
		backbutton.place(x=400,y=350)

		opt_menu.mainloop()

def reopen_login():
	tkinter.messagebox.showinfo("Login","Admin Logout Successful!")
	opt_menu.destroy()

	f7=open('CaseIndex.txt','r')
	lines1=f7.readlines()
	f7.close()
	f8=open('CaseIndex.txt','w')
	for line1 in lines1:
		if line1.startswith('*'):
			continue
		else:
			f8.write(line1)
	f8.close()

	login_in()


def key_sort(fname):
	t=list()
	fin=open(fname,'r')
	for line in fin:
		line=line.rstrip('\n')
		words=line.split('|')
		t.append((words[0],words[1]))
	fin.close()
	t.sort()
	with open("temp.txt",'w') as fout:
		for pkey,addr in t:
			pack=pkey+"|"+addr+"|$"
			fout.write(pack+'\n')
	os.remove(fname)
	os.rename("temp.txt",fname)


def binary_search(fname, search_key):
	t = []
	fin = open(fname,'r')
	for lx in fin:
		lx = lx.rstrip()
		wx = lx.split('|')
		t.append((wx[0], wx[1]))
	fin.close()
	l = 0
	r = len(t) - 1
	while l <= r:
		mid = (l + r)//2
		if t[mid][0] == search_key:
			return int(t[mid][1])
		elif t[mid][0] <= search_key:
			l = mid + 1
		else:
			r = mid - 1
	return -1

def filecomp(filename,filename2):
	f1=open(filename,'r')
	text=f1.read()
	f1.close()

	code=base64.b64encode(zlib.compress(text.encode('utf-8'),9))
	code=code.decode('utf-8')

	f2=open(filename2,'a')
	f2.write(code)
	f2.close()


def add_case():
	global case_id
	global owner_name
	global offence_name
	global vehicle_number
	global amount
	global location
	global dateofcase
	global add_menu
	global statusofcase

	add_menu=Tk()
	add_menu.wm_title("ADD CASE")
	add_menu.geometry('900x500+300+100')
	add_menu.minsize(900,500)
	add_menu.maxsize(900,500)
	add_menu.resizable(0,0)
	add_menu.configure(bg='#FF8B8B')
	# add_menu = Canvas(add_menu,width = 900, height = 500)
	# add_menu.pack()
	# image = PhotoImage(file='C:\\Users\\ullas\\Desktop\\traffic-pro\\images\\bg2.png')
	# add_menu.create_image(0,0,anchor = NW, image = image)
	
	k_font = tkinter.font.Font(family='Times New Roman', size=15, weight=tkinter.font.BOLD)

	case_detail_label=Label(add_menu,text="ADD CASE DETAILS",font="Times 30 italic bold",fg='black',bg='#B2C8DF',relief='solid')
	case_detail_label.place(x=300,y=10)

	case_id_label=Label(add_menu,text="Case ID",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
	case_id_label.place(x=260,y=80)

	owner_label=Label(add_menu,text="Owner Name",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
	owner_label.place(x=260,y=130)

	offence_label=Label(add_menu,text="Offence",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
	offence_label.place(x=260,y=180)

	vehicle_number_label=Label(add_menu,text="Vehicle Number",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
	vehicle_number_label.place(x=260,y=230)

	fine_label=Label(add_menu,text="Fine",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
	fine_label.place(x=260,y=280)

	location_label=Label(add_menu,text="Location",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
	location_label.place(x=260,y=330)

	now = datetime.now()
	date_time_str = now.strftime("%d/%m/%Y")

	date_label=Label(add_menu,text="Date",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
	date_label.place(x=260,y=380)

	status_label=Label(add_menu,text="Status",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
	status_label.place(x=260,y=420)
	

	case_id=Entry(add_menu,width=15,font=('Montserrat 15'))
	case_id.place(x=550,y=85)

	owner_name=Entry(add_menu,width=15,font=('Montserrat 15'))
	owner_name.place(x=550,y=135)

	offence_name=ttk.Combobox(add_menu,width=23,font=('Montserrat 15 '))
	offence_name['values']=['Driving/Riding without Licence','Driving without insurance','Over speeding','Driving without registration','Driving without seatbelt','Driving without Helmet','Overloading','Overloading of two-wheelers']
	offence_name.place(x=550,y=185)

	vehicle_number=Entry(add_menu,width=15,font=('Montserrat 15'))
	vehicle_number.place(x=550,y=235)

	amount=ttk.Combobox(add_menu,width=12,font=('Montserrat 15 '))
	amount['values']=['500','1000','1500','2000','3000']
	amount.place(x=550,y=285)

	location=Entry(add_menu,width=15,font=('Montserrat 15'))
	location.place(x=550,y=335)

	
	dateofcase=ttk.Combobox(add_menu,width=15,font=('Montserrat 15 '))
	dateofcase['values']=[date_time_str]
	dateofcase.place(x=550,y=385)

	statusofcase = ttk.Combobox(add_menu,width=15,font=('Montserrat 15 '))
	statusofcase['values']=['Paid','Unpaid']
	statusofcase.place(x=550,y=425)

	addbutton1=Button(add_menu,command=add_check,text=" Add Case ",bg='light blue',height=1,width=12,font=k_font)
	addbutton1.place(x=400,y=460)

	add_menu.mainloop()

def isValidLicenseNo(str):
	regex = ("^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$")
	p = re.compile(regex)
	if (str == None):
		return False
	if(re.search(p, str)):
		return True
	else:
		return False

def isValidDate(str):
	regex = ("^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$")
	p = re.compile(regex)
	if (str == None):
		return False
	if(re.search(p, str)):
		return True
	else:
		return False

def add_check():
	global b_id
	b_id=case_id.get()
	b_name=owner_name.get().upper()
	vehicle_id=vehicle_number.get().upper()
	off_name=offence_name.get().upper()
	fine=amount.get()
	location_name=location.get().upper()
	offence_date=dateofcase.get()
	case_status=statusofcase.get()

	if len(b_id)<1 or b_id.isdigit()==False:
		tkinter.messagebox.showinfo("Add Case ID","Please renter the details (ID should be 5 positive integers)")
		add_menu.lift()
		return(add_case)

	if len(b_name)==0:
		tkinter.messagebox.showinfo("Add Owner Name","You did not type a Owner name O_O")
		add_menu.lift()
		return(add_case)
	
	if len(off_name)==0:
		tkinter.messagebox.showinfo("Add Offence ","You did not type a Offence O_O")
		add_menu.lift()
		return(add_case)

	a=isValidLicenseNo(vehicle_id)

	if (a)==False:
		tkinter.messagebox.showinfo("Add Vehicle Number","You did not type a Vehicle number(KA 41 AB 1234) O_O")
		add_menu.lift()
		return(add_case)

	if len(fine)<3 and b_id.isdigit()==False:
		tkinter.messagebox.showinfo("Add Fine Amount","Please renter the Fine (Fine should be greater than 3 positive integers)")
		add_menu.lift()
		return(add_case)

	if len(location_name)==0:
		tkinter.messagebox.showinfo("Add Location ","You did not type a Location O_O")
		add_menu.lift()
		return(add_case)

	b=isValidDate(offence_date)
	
	if (b)==False:
		tkinter.messagebox.showinfo("Add Date","You did not type a Date (01/01/2000) O_O")
		add_menu.lift()
		return(add_case)
	
	pos = binary_search('CaseIndex.txt', b_id)
	if pos != -1:
		tkinter.messagebox.showinfo("Case Id","Case ID already present. Please try again")
		add_menu.lift()
		return(add_case)

	f44=open('MainCaseIndex.txt','a+')
	f55=open('MainCaseData.txt','a+')
	f22 = open ('CaseData.txt', 'a+')
	pos = f22.tell()
	f33 = open ('CaseIndex.txt', 'a+')
	buf = b_id + '|' + b_name + '|' + vehicle_id + '|' + off_name + '|' + fine + '|' + location_name + '|' + offence_date + '|'  + case_status + '|'+'$'
	f22.write(buf)
	f22.write('\n')
	buf = b_id + '|' + b_name + '|' + vehicle_id + '|' + off_name + '|' + fine + '|' + location_name + '|' + offence_date + '|'  + case_status + '$'
	f55.write(buf)
	f55.write('\n')
	buf = b_id + '|' + str(pos) + '|' + '$'
	f33.write(buf)
	f33.write('\n')
	buf= b_id + '|'+ str(pos) + '$'
	f44.write(buf)
	f44.write('\n')
	f33.close()
	f22.close()
	f55.close()
	f44.close()
	key_sort('CaseIndex.txt')
	filecomp('CaseData.txt','CompressedCaseData.txt')

	def hash_file(i):
		h=hlib.sha1()
		with open(i,'rb')as file:
			c=0
			while c!=b'':
				c=file.read(1024)
				h.update(c)
		return h.hexdigest()
	message=hash_file("Casedata.txt")+ '|'+ b_id + '$'
	print(message)
	f10=open('HashedData.txt','a+',newline='')
	f10.write(message+'\n')
	f10.close()
	
	tkinter.messagebox.showinfo("ADD","Case Details added Successfully!")

	add_menu.destroy()


def del_case():
	global rb_id
	global del_menu

	del_menu=Tk()
	del_menu.wm_title("Delete Case")
	del_menu.geometry('900x500+300+100')
	del_menu.minsize(900,500)
	del_menu.maxsize(900,500)
	del_menu.resizable(0,0)
	del_menu.configure(bg='#B7D3DF')
	# del_menu = Canvas(del_menu,width=900,height=500)
	# del_menu.pack()
	# image = PhotoImage(file='C:\\Users\\ullas\\Desktop\\traffic-pro\\images\\bg2.png')
	# del_menu.create_image(0,0,anchor = NW, image = image)
	
	k_font = tkinter.font.Font(family='Times New Roman', size=15, weight=tkinter.font.BOLD)

	C_Id=[]
	O_Name = []
	Offence = []
	V_Number = []
	F_Amount = []
	Loc = []
	C_Date = []
	C_status=[]


	f1 = open('CaseIndex.txt', 'r')
	f = open ("CaseData.txt", 'r')
	norecord = 0
	for line in f1:
		if not line.startswith('*'):
			norecord += 1
			line = line.rstrip('\n')
			word = line.split('|')
			f.seek(int(word[1]))
			line1 = f.readline().rstrip()
			word1 = line1.split('|')
			C_Id.append(word1[0])
			O_Name.append(word1[1])
			V_Number.append(word1[2])
			Offence.append(word1[3])
			F_Amount.append(word1[4])
			Loc.append(word1[5])
			C_Date.append(word1[6])
			C_status.append(word1[7])
	f.close()

	case_list=Listbox(del_menu,height=50,width=15)
	case_list2=Listbox(del_menu,height=50,width=15)
	case_list3=Listbox(del_menu,height=50,width=20)
	case_list4=Listbox(del_menu,height=50,width=31)
	case_list5=Listbox(del_menu,height=50,width=17)
	case_list6=Listbox(del_menu,height=50,width=17)
	case_list7=Listbox(del_menu,height=50,width=13)
	case_list8=Listbox(del_menu,height=50,width=15)

	for num in range(0,norecord):
		case_list.insert(0,C_Id[num])
		case_list2.insert(0,O_Name[num])
		case_list3.insert(0,V_Number[num])
		case_list4.insert(0,Offence[num])
		case_list5.insert(0,F_Amount[num])
		case_list6.insert(0,Loc[num])
		case_list7.insert(0,C_Date[num])
		case_list8.insert(0,C_status[num])


	b_label=Label(del_menu,text="CASE ID",fg='#EAF6F6',bg='#FF0063', font="Times 20 italic bold")
	rb_id=Entry(del_menu,width=15,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
	delbutton1=Button(del_menu,command=del_check,text="DELETE",bg='red',height=1,width=12,font=k_font)
	
	case_list.configure(background="light grey")
	case_list2.configure(background="light blue")
	case_list3.configure(background="light green")
	case_list4.configure(background="light grey")
	case_list5.configure(background="light blue")
	case_list6.configure(background="light green")
	case_list7.configure(background="light grey")
	case_list8.configure(background="light blue")

	case_label=Label(del_menu,text="Case Id", font="Times 13 italic bold")
	case_label2=Label(del_menu,text="Owner Name", font="Times 13 italic bold")
	case_label3=Label(del_menu,text="Vehicle Number", font="Times 13 italic bold")
	case_label4=Label(del_menu,text="Offence", font="Times 13 italic bold")
	case_label5=Label(del_menu,text="Fine Amount", font="Times 13 italic bold")
	case_label6=Label(del_menu,text="Location", font="Times 13 italic bold")
	case_label7=Label(del_menu,text="Date", font="Times 13 italic bold")
	case_label8=Label(del_menu,text="Status", font="Times 13 italic bold")

	case_label.grid(row=9,column=0)
	case_label2.grid(row=9,column=1)
	case_label3.grid(row=9,column=2)
	case_label4.grid(row=9,column=3)
	case_label5.grid(row=9,column=4)
	case_label6.grid(row=9,column=5)
	case_label7.grid(row=9,column=6)
	case_label8.grid(row=9,column=7)

	case_list.grid(row=10,column=0)
	case_list2.grid(row=10,column=1)
	case_list3.grid(row=10,column=2)
	case_list4.grid(row=10,column=3)
	case_list5.grid(row=10,column=4)
	case_list6.grid(row=10,column=5)
	case_list7.grid(row=10,column=6)
	case_list8.grid(row=10,column=7)
	b_label.grid(row=0,column=1,sticky=E)
	rb_id.grid(row=0,column=3)
	delbutton1.grid(row=0,column=5,columnspan=1)

	del_menu.mainloop()

def del_check():

	global del_id
	del_id=rb_id.get()

	if len(del_id)==0:
		tkinter.messagebox.showinfo("Delete Case","You did not type anything O_O")
		del_menu.lift()
		return(del_case)

	pos = binary_search('CaseIndex.txt', del_id)
	if(pos == -1):
		tkinter.messagebox.showinfo("Delete","Case Id not present.Please reenter")
		del_menu.destroy()
		return(del_case)
	else:
		f = open ('CaseData.txt', 'r')
		f.seek(pos)
		l1 = f.readline().rstrip()
		w1 = l1.split('|')
		if(w1[7] == 'Unpaid'):
			tkinter.messagebox.showinfo("Delete","Processing Payment. Please try another case")
			del_menu.destroy()
			return(del_case)

	index = -1

	with open('CaseIndex.txt','r') as file:
		for line in file:
			words=line.split("|")
			if(words[0]==del_id):
					index=int(words[1])

	index=0
	with open("CaseIndex.txt",'r+') as file:
		line=file.readline()
		while line:
			words=line.split("|")
			if words[0]==del_id:
				file.seek(index,0)
				file.write("*")
				break
			else:
				index=file.tell()
				line=file.readline()
	tkinter.messagebox.showinfo("Delete","Case Successfully removed")
	del_menu.destroy()



def Main_Menu():
	base = Tk()
	base.wm_title("USER MAIN MENU ")
	base.geometry('900x500+300+100')
	base.minsize(900,500)
	base.maxsize(900,500)
	base.resizable(0,0)
	base.configure(bg='light blue')
	# base = Canvas(base,width=900,height=500)
	# base.pack()
	# image = PhotoImage(file='C:\\Users\\ullas\\Desktop\\traffic-pro\\images\\bg2.png')
	# base.create_image(0,0,anchor = NW, image = image)

	in_font = tkinter.font.Font(family='Times New Roman', size=15, weight=tkinter.font.BOLD)
	current_time1=datetime.now()
	current_time=str(current_time1)

	
	status = Label(base,text=("Date and time logged in: " + current_time),bd=1,relief=SUNKEN,anchor=W,bg='#66BFBF')
	orionLabel=Label(base, text="TRAFFIC VIOLATION MANAGEMENT ",font="Times 30 italic bold",fg='black',bg='#66BFBF',relief='solid',width=32)
	welcomeLabel=Label(base,text=("Logged in as "+name.upper() +"   (ID : "+id+")"),font=("Times new roman","20","bold"),bg='light green')
	topFrame=Frame(base)
	bottomFrame=Frame(base)

	status.pack(side=BOTTOM,fill=X)
	orionLabel.pack(fill=X)
	welcomeLabel.pack(fill=X)
	topFrame.pack()
	bottomFrame.pack(side=BOTTOM)

	purchase_but=Button(base,bg="#FF8B8B",fg="white",text="Pay Fine Amount",font=in_font,height=5,width=15,command=purchase_in)
	search_but=Button(base,bg="#FF8B8B",fg="white",text="Search Case",font=in_font,height=5,width=15,command=search_in)
	

	purchase_but.place(x=300,y=180)
	search_but.place(x=500,y=180)
	
	base.mainloop()


def purchase_in():
	global purchase_entry1
	global case_menu

	case_menu=Tk()

	case_menu.wm_title("Pay Fine ")
	case_menu.geometry('900x500+300+100')
	case_menu.minsize(900,500)
	case_menu.maxsize(900,500)
	case_menu.resizable(0,0)
	case_menu.configure(bg='#B7D3DF')
	# case_menu = Canvas(case_menu,width = 900, height = 500)
	# case_menu.pack()
	

	C_Id=[]
	O_Name = []
	Offence = []
	V_Number = []
	F_Amount = []
	Loc = []
	C_Date = []
	C_status=[]
	

	f1 = open('CaseIndex.txt', 'r')
	f = open ("CaseData.txt", 'r')
	norecord = 0
	for line in f1:
		norecord += 1
		line = line.rstrip('\n')
		word = line.split('|')
		f.seek(int(word[1]))
		line1 = f.readline().rstrip()
		word1 = line1.split('|')
		C_Id.append(word1[0])
		O_Name.append(word1[1])
		V_Number.append(word1[2])
		Offence.append(word1[3])
		F_Amount.append(word1[4])
		Loc.append(word1[5])
		C_Date.append(word1[6])
		C_status.append(word1[7])

	f.close()

	case_list=Listbox(case_menu,height=50,width=15)
	case_list1=Listbox(case_menu,height=50,width=15)
	case_list2=Listbox(case_menu,height=50,width=20)
	case_list3=Listbox(case_menu,height=50,width=31)
	case_list4=Listbox(case_menu,height=50,width=17)
	case_list5=Listbox(case_menu,height=50,width=17)
	case_list6=Listbox(case_menu,height=50,width=13)
	case_list7=Listbox(case_menu,height=50,width=15)

	for num in range(0,norecord):
		case_list.insert(0,C_Id[num])
		case_list1.insert(0,O_Name[num])
		case_list2.insert(0,V_Number[num])
		case_list3.insert(0,Offence[num])
		case_list4.insert(0,F_Amount[num])
		case_list5.insert(0,Loc[num])
		case_list6.insert(0,C_Date[num])
		case_list7.insert(0,C_status[num])

	k_font = tkinter.font.Font(family='Times New Roman', size=15, weight=tkinter.font.BOLD)

	case_list.configure(background="light grey")
	case_list1.configure(background="light blue")
	case_list2.configure(background="light green")
	case_list3.configure(background="light grey")
	case_list4.configure(background="light blue")
	case_list5.configure(background="light green")
	case_list6.configure(background="light grey")
	case_list7.configure(background="light blue")

	case_label=Label(case_menu,text="Case Id", font="Times 13 italic bold")
	case_label1=Label(case_menu,text="Owner Name", font="Times 13 italic bold")
	case_label2=Label(case_menu,text="Vehicle Number", font="Times 13 italic bold")
	case_label3=Label(case_menu,text="Offence", font="Times 13 italic bold")
	case_label4=Label(case_menu,text="Fine Amount", font="Times 13 italic bold")
	case_label5=Label(case_menu,text="Location", font="Times 13 italic bold")
	case_label6=Label(case_menu,text="Date", font="Times 13 italic bold")
	case_label7=Label(case_menu,text="Status", font="Times 13 italic bold")

	case_label9=Label(case_menu,text="Please enter the Case ID that you wish to Pay",font="Times 20 italic bold",fg='black',bg='#B2C8DF',relief='solid')
	purchase_entry1=Entry(case_menu,width=15,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
	purchase_button1=Button(case_menu,text="P a y",command=purchase_check,height=1,width=12,bg="red",font=k_font)

	case_label9.grid(row=0,columnspan=20)
	purchase_entry1.grid(row=4,columnspan=5)
	purchase_button1.grid(row=4,columnspan=15,column=2)
	
	case_label.grid(row=9,column=0)
	case_label1.grid(row=9,column=1)
	case_label2.grid(row=9,column=2)
	case_label3.grid(row=9,column=3)
	case_label4.grid(row=9,column=4)
	case_label5.grid(row=9,column=5)
	case_label6.grid(row=9,column=6)
	case_label7.grid(row=9,column=7)

	case_list.grid(row=10,column=0)
	case_list1.grid(row=10,column=1)
	case_list2.grid(row=10,column=2)
	case_list3.grid(row=10,column=3)
	case_list4.grid(row=10,column=4)
	case_list5.grid(row=10,column=5)
	case_list6.grid(row=10,column=6)
	case_list7.grid(row=10,column=7)

	case_menu.mainloop()

def purchase_check():

	count = 0
	f = open('Record.txt', 'r')
	for l in f:
		l = l.split('|')
		if l[0] ==  id:
			count += 1
	if count >= 3:
		tkinter.messagebox.showinfo("select", "Cannot purchase more than 3 products")
		case_menu.destroy()

	else:
		pproduct=purchase_entry1.get()

		if len(pproduct) == 0:
			tkinter.messagebox.showinfo("select","You did not type anything O_O")
			case_menu.lift()
			return(purchase_in)

		pos = binary_search('CaseIndex.txt', pproduct)
		if pos == -1:
			tkinter.messagebox.showinfo("select","The Case that you had entered is not in our database,sorry,please enter a different Case")
			case_menu.lift()
		else:
			f2 = open('CaseData.txt', 'r+')
			f2.seek(pos)
			l2 = f2.readline()
			l2 = l2.rstrip('\n')
			w2 = l2.split('|')
			if(str(w2[7]) == "Unpaid"):
				l3 = w2[0] + '|' + w2[1] + '|' + w2[2] + '|' + w2[3]+ '|' + w2[4]+ '|' + w2[5]+ '|' + w2[6]+ '|'+ 'Paid|$'
				f2.seek(pos)
				f2.write(l3)
				f2.close()
				tkinter.messagebox.showinfo("Pay","The case you have selected has been successfully paid. " )

				buf = id + '|' + pproduct + '|$\n'
				f3 = open('Record.txt', 'a')
				f3.write(buf)
				f3.close()
				key_sort('Record.txt')
				Done2=tkinter.messagebox.askyesno("Pay","Do you want to pay for another case?")
				if Done2==True:
					case_menu.destroy()
					purchase_in()
				else:
					case_menu.destroy()
			else:
				tkinter.messagebox.showinfo("Pay","This case is currently unavailable, please select another case")
				case_menu.lift()


# def return_in():
# 	global return_entry1
# 	global return_menu
# 	global record_verification

# 	return_menu=Tk()
# 	return_menu.wm_title("Pay Fine")
# 	return_menu.geometry('900x500+300+100')
# 	return_menu.resizable(0,0)
# 	return_menu.configure(bg='blue')
# 	return_menu = Canvas(return_menu,width = 900, height = 500)
# 	return_menu.pack()

# 	C_Id=[]
# 	O_Name = []
# 	Offence = []
# 	V_Number = []
# 	F_Amount = []
# 	Loc = []
# 	C_Date = []
# 	C_status=[]
# 	record_verification = []

# 	f = open ('Record.txt')
# 	norecord = 0
# 	for line in f:
# 		line = line.rstrip()
# 		words = line.split('|')
# 		if(words[0] == id):
# 			pos = binary_search('CaseIndex.txt', words[1])
# 			if pos != -1:
# 				norecord += 1
# 				f2 = open('CaseData.txt', 'r')
# 				f2.seek(pos)
# 				l1 = f2.readline()
# 				l1 = l1.rstrip()
# 				w1 = l1.split('|')
# 				C_Id.append(w1[0])
# 				O_Name.append(w1[1])
# 				V_Number.append(w1[2])
# 				Offence.append(w1[3])
# 				F_Amount.append(w1[4])
# 				Loc.append(w1[5])
# 				C_Date.append(w1[6])
# 				C_status.append(w1[7])
# 				record_verification.append(w1[0])
				
# 	f.close()

# 	return_list=Listbox(return_menu,height=50,width=15)
# 	return_list1=Listbox(return_menu,height=50,width=15)
# 	return_list2=Listbox(return_menu,height=50,width=20)
# 	return_list3=Listbox(return_menu,height=50,width=31)
# 	return_list4=Listbox(return_menu,height=50,width=17)
# 	return_list5=Listbox(return_menu,height=50,width=17)
# 	return_list6=Listbox(return_menu,height=50,width=13)
# 	return_list7=Listbox(return_menu,height=50,width=15)
	

# 	for num in range(0,norecord):
# 		return_list.insert(0,C_Id[num])
# 		return_list1.insert(0,O_Name[num])
# 		return_list2.insert(0,V_Number[num])
# 		return_list3.insert(0,Offence[num])
# 		return_list4.insert(0,F_Amount[num])
# 		return_list5.insert(0,Loc[num])
# 		return_list6.insert(0,C_Date[num])
# 		return_list7.insert(0,C_status[num])

# 	k_font = tkinter.font.Font(family='Times New Roman', size=15, weight=tkinter.font.BOLD)

# 	return_button1=Button(return_menu,text="PAY",command=return_check,height=1,width=12,bg="#834c9c",font=k_font)
# 	return_entry1=Entry(return_menu,width=15,font=('Montserrat 15'))
# 	return_label9=Label(return_menu,text=" Please enter the CASE ID that you wish to pay ",font="Times 20 italic bold",bg="#834c9c")

# 	return_list.configure(background="light grey")
# 	return_list1.configure(background="light blue")
# 	return_list2.configure(background="light green")
# 	return_list3.configure(background="light grey")
# 	return_list4.configure(background="light blue")
# 	return_list5.configure(background="light green")
# 	return_list6.configure(background="light grey")
# 	return_list7.configure(background="light blue")

# 	return_label=Label(return_menu,text="Case Id", font="Times 13 italic bold")
# 	return_label1=Label(return_menu,text="Owner Name", font="Times 13 italic bold")
# 	return_label2=Label(return_menu,text="Vehicle Number", font="Times 13 italic bold")
# 	return_label3=Label(return_menu,text="Offence", font="Times 13 italic bold")
# 	return_label4=Label(return_menu,text="Fine Amount", font="Times 13 italic bold")
# 	return_label5=Label(return_menu,text="Location", font="Times 13 italic bold")
# 	return_label6=Label(return_menu,text="Date", font="Times 13 italic bold")
# 	return_label7=Label(return_menu,text="Status", font="Times 13 italic bold")

	
	

# 	return_label.grid(row=9,column=0)
# 	return_label1.grid(row=9,column=1)
# 	return_label2.grid(row=9,column=2)
# 	return_label3.grid(row=9,column=3)
# 	return_label4.grid(row=9,column=4)
# 	return_label5.grid(row=9,column=5)
# 	return_label6.grid(row=9,column=6)
# 	return_label7.grid(row=9,column=7)

# 	return_list.grid(row=10,column=0)
# 	return_list1.grid(row=10,column=1)
# 	return_list2.grid(row=10,column=2)
# 	return_list3.grid(row=10,column=3)
# 	return_list4.grid(row=10,column=4)
# 	return_list5.grid(row=10,column=5)
# 	return_list6.grid(row=10,column=6)
# 	return_list7.grid(row=10,column=7)

# 	return_label9.grid(row=0,columnspan=20)
# 	return_entry1.grid(row=4,columnspan=5)
# 	return_button1.grid(row=4,column=2,columnspan=10)

# 	return_menu.mainloop()


# def return_check():
# 	import datetime as dt
# 	from datetime import timedelta
# 	date = dt.date.today()
# 	pproduct = return_entry1.get().upper()

# 	if len(pproduct) == 0:
# 		tkinter.messagebox.showinfo("Return","You did not type anything O_O")
# 		return_menu.lift()
# 		return(return_in)

# 	if(pproduct in record_verification):
# 		pos = binary_search('CaseIndex.txt', pproduct)
# 		if pos != -1:
# 			f1 = open('CaseData.txt', 'r+')
# 			f1.seek(pos)
# 			l1 = f1.readline().rstrip()
# 			w1 = l1.split('|')
# 			if(w1[7] == 'Paid'):
# 				tkinter.messagebox.showinfo("Return","The Case you have selected has been successfully paid"+'\n'+str(date))
# 				f1.seek(pos)
# 				line = w1[0] + '|' + w1[1] + '|' + w1[2]+ '|' + w1[3]+ '|' + w1[4]+ '|' + w1[5]+ '|' + w1[6]+ '|' + '|Paid|#'
# 				f1.write(line)

# 				f2=open('Record.txt','r')
# 				lines=f2.readlines()
# 				f2.close()
# 				f3=open('Record.txt','w')
# 				for l2 in lines:
# 					l3=l2.split('|')
# 					if l3[1] == pproduct and l3[0] == id:
# 						continue
# 					else:
# 						f3.write(l2)
# 				f3.close()
# 				Done3=tkinter.messagebox.askyesno("Return","Do you want to pay fine for another case?")
# 				if Done3==True:
# 					f1.close()
# 					return_menu.destroy()
# 					return_in()
# 				else:
# 					return_menu.destroy()
# 			else:
# 				tkinter.messagebox.showinfo("This case has been paid, please select another case")
# 			f1.close()
# 	else:
# 		tkinter.messagebox.showinfo("Return","The case id that you had entered is invalid.Please reenter a different case id")
# 		return_menu.lift()


def search_in():
	global search_entry
	global search_menu
	search_menu=Tk()

	search_menu.wm_title("Search Case")
	search_menu.geometry('900x200+300+100')
	search_menu.minsize(900,200)
	search_menu.maxsize(900,200)
	search_menu.resizable(0,0)
	search_menu.configure(bg='#66BFBF')
	# search_menu = Canvas(search_menu,width = 900, height = 200)
	# search_menu.pack()
	# image = PhotoImage(file='C:\\Users\\ullas\\Desktop\\traffic-pro\\images\\bg2.png')
	# search_menu.create_image(0,0,anchor = NW, image = image)

	k_font = tkinter.font.Font(family='Times New Roman', size=15, weight=tkinter.font.BOLD)

	search_label1=Label(search_menu,text="Search through our database to check if your case is available", font="Times 20 italic bold",fg='black',bg='#B2C8DF',relief='solid')
	search_label1.place(x=100,y=10)

	search_entry = Entry(search_menu,width=15,font=('Montserrat 15'),relief='solid',borderwidth=2,bg='light grey')
	search_entry.place(x=350,y=70)

	search_button=Button(search_menu,text="Search",command=search_check,font=k_font,bg='light green',height=1,width=12)
	search_button.place(x=375,y=120)

	search_menu.mainloop()


def search_check():
	search_word=search_entry.get().upper()
	search_menu.destroy()

	if len(search_word) == 0:
		tkinter.messagebox.showinfo("Search","You did not type anything O_O")
		return(search_in)

	pos = binary_search('CaseIndex.txt', search_word)

	if (pos == -1):
		tkinter.messagebox.showinfo("Search","Sorry,this Case ID does not exist in our database")
	else:
		search_menu2=Tk()
		search_menu2.wm_title("Search")
		search_menu2.attributes("-topmost",True)
		tkinter.messagebox.showinfo("Search","It is in our database!")

		search_result=Listbox(search_menu2,height=15,width=80)
		search_result.place(x=300,y=100)
		search_result.configure(bg='light blue')
		f2 = open('CaseData.txt', 'r')
		f2.seek(pos)
		l1 = f2.readline()
		l1 = l1.rstrip()
		w1 = l1.split('|')
		C_id = w1[0]
		O_Name = w1[1]
		V_Number = w1[2]
		Offence=w1[3]
		F_Amount=w1[4]
		Loc=w1[5]
		C_Date=w1[6]
		
		if(w1[7] == 'Paid'):
			C_status = 'Paid'
		else:
			C_status = 'Unpaid'
		f2.close()

		search_result.insert(1,"Case ID: " + C_id)
		search_result.insert(2,"Owner Name: " + O_Name)
		search_result.insert(3,"Vehicle Number: " + V_Number)
		search_result.insert(4,"Offence: " + Offence)
		search_result.insert(5,"Fine Amount: " + F_Amount)
		search_result.insert(6,"Location: " + Loc)
		search_result.insert(7,"Date: " + C_Date)
		search_result.insert(8,"Status: " + C_status)
		

		search_result.pack()
		search_menu2.mainloop()

login_in()


