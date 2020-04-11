import sys 

def login_screen():
	name = input("Name: ")
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
	temp=0
	z =0 
	for i in range(len(name_list)):
		if (name == name_list[i]) and (pwd == pwd_list[i]):
			main_menu(name)
			break
	print("Module Record System -Options")

def main_menu(name):
	print(f"\nWelcome {name}")
	while True:
		print("\nModule Record System - Options")
		print("-"*20)
		print("1. Record Attendance")
		print("2. Generate Statistics")
		print("3. Exit")
		menu = input("> ")

		if menu == "1":
			print("Recording Attendance")
		elif menu == "2":
			print("Generate Statistics")
		elif menu == "3":
			break
		else:
			print("\nPlease choose valid option")			

	sys.exit()
			
def main():
	login_screen()

main()	