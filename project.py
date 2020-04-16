import sys #importing sys to be able to exit app on invalid creditentials in login function

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
	menu_module = input("> ")
	return 

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
			load_module("Attendance")
		elif menu == "2":
			load_module("Statistics")
		elif menu == "3":
			break
		else:
			print("\nPlease choose valid option")			
			
def main():
	name = login()
	main_menu(name)

main()	