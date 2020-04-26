#App created by: Andrzej Sokolowski
#R00184058
#github: https://github.com/ghoasta/Project2020

import sys #importing sys to be able to exit app on invalid creditentials in login function
import datetime #importing to get the todays date

def str_list_to_int_list(str_list):#function to convert string list to int list
    i = 0
    while i < len(str_list):
        str_list[i] = int(str_list[i])
        i += 1
    return str_list 

def create_student_list(filename):#function to create all lits used by app
	student_list = []
	present_list = []
	absent_list = []
	excused_list = []

	with open (filename,'r') as f:#slicing and creating lists
		for line in f:
			x = (line.split(',')[0].rstrip())
			y = (line.split(',')[1].rstrip())
			z = (line.split(',')[2].rstrip())
			q = (line.split(',')[3].rstrip())
			student_list.append(x)
			present_list.append(y)
			absent_list.append(z)
			excused_list.append(q)
	#converting to int
	present_list = str_list_to_int_list(present_list)
	absent_list = str_list_to_int_list(absent_list)
	excused_list = str_list_to_int_list(excused_list)
	#calculating 70%
	total_days= present_list[0]+excused_list[0]+absent_list[0]
	target_percent = (70 * total_days)/100

	return student_list,present_list,absent_list,excused_list,target_percent,total_days		

def take_class_attendance(filename,module_code,purpose):#taking the attendance,saving it to lists and saving back to file
	print(f"\nModule Record System({purpose}) {module_code}")
	print("-"*30)
	student_list,present_list,absent_list,excused_list,target_percent,total_days = create_student_list(filename)
	print(f"There are {len(student_list)} students enrolled.")

	for i in range(len(student_list)):
		while True:
			print(f"Student #{i+1}: {student_list[i]}")
			print("1. Present")
			print("2. Absent")
			print("3. Excused")
			atten = input("> ")
			if atten == "1":
				present_list[i]+=1
				break
			elif atten == "2":
				absent_list[i]+=1
				break
			elif atten == "3":
				excused_list[i]+=1
				break
			else:
				print("Valid number only")	
	#saving to file
	output = open(filename,'w')
	for i in range(len(student_list)):
		print((student_list[i]+","+str(present_list[i])+","+str(absent_list[i])+","+str(excused_list[i])),file=output)

def non_attander(student_list,present_list):#calculating students who did not attend
	non_attander =[]
	for i in range(len(student_list)):
		if present_list[i] == 0:
			non_attander.append(student_list[i])
	if not non_attander:
		non_attander.append("None")
	return non_attander	

def calc_seventy_percent(student_list,absent_list,total_days,target_percent):#calculating 70%
	below_seventy = []
	for i in range(len(absent_list)):
		if absent_list[i] > (total_days - target_percent):
			below_seventy.append(student_list[i])
	return below_seventy			

def calc_best_attendance(student_list,present_list,total_days):#calculating best attender
	best_attendance = []
	max_days = max(present_list)
	for i in range(len(present_list)):
		if present_list[i] == max_days:
			best_attendance.append(student_list[i])
	return	best_attendance		


def get_class_attendance(filename,module_code,purpose):#reading the attendance and saving stats file
	student_list,present_list,absent_list,excused_list,target_percent,total_days = create_student_list(filename)
	new_filename = module_code+"_"+(datetime.date.today().strftime("%d-%m-%Y"))+".txt"
	below = (', '.join(calc_seventy_percent(student_list,absent_list,total_days,target_percent)))
	none = (', '.join(non_attander(student_list,present_list)))
	best = (', '.join(calc_best_attendance(student_list,present_list,total_days)))
	average = sum(present_list)/len(present_list)
	output = open(new_filename,'w')
	
	print(f"Module: {module_code}")
	print(f"Module: {module_code}",file=output)
	print(f"Number of students: {len(student_list)}")
	print(f"Number of students: {len(student_list)}",file=output)
	print(f"Number of classes: {max(present_list)}")
	print(f"Number of classes: {max(present_list)}",file=output)
	print("Avarage Attendance: {:0,.1f} days".format(average))
	print("Avarage Attendance: {:0,.1f} days".format(average),file=output)
	print(f"Low Attender(s): under 70.0 %")
	print(f"Low Attender(s): under 70.0 %",file=output)
	print(f"\t{below}")
	print(f"\t{below}",file=output)
	print(f"Non Attender(s):")
	print(f"Non Attender(s):",file=output)
	print(f"\t{none}")
	print(f"\t{none}",file=output)
	print(f"Best Attender(s):")
	print(f"Best Attender(s):",file=output)
	print(f"\tAttended {max(present_list)}/{total_days} days")
	print(f"\tAttended {max(present_list)}/{total_days} days",file=output)
	print(f"\t{best}")
	print(f"\t{best}",file=output)

def load_module(purpose):#function to load module from module.txt
	print(f"\nModule Record System({purpose}) - Choose a Module")
	print("-"*30)	
	modules_list = []
	while True:
		with open('modules.txt','r') as f:	#displaying the modules code from modules.txt
			for line in f:
				x = (line.split(',')[0])
				modules_list.append(x)	
		for i in range(len(modules_list)):
			print(f"{i+1}. {modules_list[i]}")		
		menu_module = input("> ")
		if ((menu_module == "1") or (menu_module == "2")):
			m = int(menu_module)
			filename = modules_list[m-1]+".txt"
			module_code = modules_list[m-1]
			break
		else:
			modules_list = []
			print("Please choose valid option")
	return filename,module_code

def login():#login finction
	name = input("\nName: ")
	pwd = input("Password: ")
	connection = open("login_data.txt")
	name_list = []
	pwd_list = []
	while True:
		line = connection.readline().rstrip()
		if line == "":
			break
		name_list.append(line)
		line = connection.readline().rstrip()
		pwd_list.append(line)
		temp = -1
	for i in range(len(name_list)):
		if (name == name_list[i]) and (pwd == pwd_list[i]):
			temp = i
	if temp == -1:		
		sys.exit("\nModule Record System – Login Failed")#exit
	else: 
		return name_list[temp]	

def main_menu(name): #main function to display main menu
	print(f"\nWelcome {name}")
	while True:
		print("\nModule Record System - Options")
		print("-"*20)
		print("1. Record Attendance")
		print("2. Generate Statistics")
		print("3. Exit")
		menu = input("> ")

		if menu == "1":
			filename , module_code = load_module("Attendance")
			take_class_attendance(filename,module_code,"Attendance")
		elif menu == "2":
			filename , module_code = load_module("Statistics")
			get_class_attendance(filename,module_code,"Statistics")
		elif menu == "3":
			break
		else:
			print("\nPlease choose valid option")			
			
def main():#main function, just to call login and main menu
	name = login()
	main_menu(name)

main()	#call main function