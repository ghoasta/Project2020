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
	for i in range(len(name_list)):
		if (name == name_list[i]) and (pwd == pwd_list[i]):
			temp=temp+1
			print(f"\nWelcome {name}")
			main_menu()
			break
		else:
			if temp!=0:
				print("Module Record System - Login Failed")	

def main_menu():
	print("\nModule Record System - Options")
	print("-"*20)
	print("1. Record Attendance")
	print("2. Generate Statiscic")
	print("3. Exit")


def main():
	login_screen()

main()	