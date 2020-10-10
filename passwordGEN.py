try:
	import random, string, os, platform, colorama, time
	from colorama import Fore, Style, init
	init()
except Exception as e:
	if platform.system() == "Windows":
		os.system('cls')
		os.system("title Creations / Password Generator")
		os.system('mode con: cols=60 lines=5')
	else:
		os.system('clear')
	print('Error Please Install colorama'.center(60))
	print('/////////////////////////////'.center(60))
	print('Example "pip install colorama"'.center(60))
	input("")
	quit()

def Setup():
	if platform.system() == "Windows":
		os.system('cls')
		os.system("title Creations / Password Genorator")
		os.system('mode con: cols=60 lines=20')
	else:
		os.system('clear')

def fix(num):
	if num % 1 == 0:
		return int(num)
	else:
		return num

def main():
	Setup()
	def get_random_string(length):
	    letters = string.ascii_letters + string.digits + string.punctuation
	    passresult = ''.join(random.choice(letters) for i in range(length))
	    print(Fore.YELLOW + passresult)
	    try:
	    	writeToFile = input(f'\n{Fore.BLUE}Would You Like To Save This to a {Fore.RED}file? {Fore.CYAN}(y/n):{Fore.YELLOW} ')
	    	if writeToFile == "y":
	    		try:
	    			Setup()
	    			UserName = input(f"{Fore.BLUE}Username:{Fore.RED} ")
	    			with open("Passwords.txt", "a+") as UserPassWords:
	    				UserPassWords.write(f'[ Username: {UserName} ] / [ Password: {passresult} ]\n')
	    			os.system('mode con: cols=70 lines=5')
	    			print(f"{Fore.CYAN}Added To The{Fore.RED} Passwords.txt{Fore.CYAN} FILE{Fore.YELLOW} With The Username {Fore.BLUE}[ {Fore.MAGENTA}{UserName}{Fore.BLUE} ]\n")
	    			time.sleep(10)
	    			main()
	    		except KeyboardInterrupt:
	    			quit()
	    	else:
	    		main()
	    except KeyboardInterrupt:
	    	quit()

	try:
		ExpectedLength = input(f"{Fore.RED}How Many Characters?:{Fore.BLUE} ")
		if int(ExpectedLength) >= 60:
			os.system(f'mode con: cols=200 lines=20')
		else:
			Setup()
	except KeyboardInterrupt:
		quit()

	try:
		get_random_string(int(ExpectedLength))
	except Exception as e:
		print("Error Not a valid NUMBER")
		quit()

main()
