import sys #importing sys to be able to exit app on invalid creditentials in login function


def create_student_list(filename):
	student_list = []
	with open (filename,'r') as f:
		for line in f:
			x = (line.split(',')[0])
			student_list.append(x)
	return student_list		


def take_class_attendance(filename,module_code,purpose):
	print(f"\nModule Record System({purpose}) {module_code}")
	print("-"*30)
	student_list = create_student_list(filename)
	print(f"There are {len(student_list)} students enrolled.")
	for i in range(len(student_list)):
		print(f"Student #{i+1}: {student_list[i]}")
		print("1. Present")
		print("2. Absent")
		print("3. Excused")
		atten = input("> ")

def get_class_attendance(filename,module_code,purpose):
	student_list = create_student_list(filename)
	print(f"Module: {module_code}")
	print(f"Number of students: {len(student_list)}")
	print(f"Number of classes: ")
	print(f"Avarage Attendance: ")
	print(f"Low Attender(s): under 70.0 %")
	print(f"")
	print(f"Non Attender(s):")
	print(f"")
	print(f"Best Attender(s):")
	print(f"")


def load_module(purpose):
	print(f"\nModule Record System({purpose}) -Choose a Module")
	print("-"*30)	
	modules_list = []
	with open('modules.txt','r') as f:	#displaying the modules code from modules.txt
		for line in f:
			x = (line.split(',')[0])
			modules_list.append(x)	
	for i in range(len(modules_list)):
		print(modules_list[i])		
	menu_module = int(input("> "))
	filename = modules_list[menu_module-1]+".txt"
	module_code = modules_list[menu_module-1]
	return filename,module_code

def login():
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
		sys.exit("\nModule Record System – Login Failed")
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
			#print(f"Filename {filename} | Module Code {module_code}")
			take_class_attendance(filename,module_code,"Attendance")
		elif menu == "2":
			filename , module_code = load_module("Statistics")
			get_class_attendance(filename,module_code,"Statistics")
			#print(f"Filename {filename} | Module Code {module_code}")
		elif menu == "3":
			break
		else:
			print("\nPlease choose valid option")			
			
def main():
	name = login()
	main_menu(name)

main()	