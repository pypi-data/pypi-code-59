# -*- coding:utf -8 -*-
import colorama
import socket


class Scanner():
	"""docstring for Scaner"""
	
	def scan_a_specific_port():
		color_a = colorama.Fore.GREEN + "[+] "
		print("~"*50)
		host = input(color_a + "Host --> ")
		port = int(input(color_a + "Port --> "))
		print("~"*50)

		scan = socket.socket()

		color_b = colorama.Fore.RED + "[!] "
		color_c = colorama.Fore.YELLOW + "[!] "

		try:
			scan.connect((host, port))
		except socket.error:
			print(color_b + "Port -- ", port, " -- [CLOSED]")
		else:
			print(color_c + "Port -- ", port, " -- [OPEN]")

	def scan_base_ports():

		colorama.init()

		color_a = colorama.Fore.GREEN + "[+] "
		color_b = colorama.Fore.RED + "[!] "
		color_c = colorama.Fore.YELLOW + "[!] "
		color_d = colorama.Fore.WHITE

		print(color_a + "Host" + color_d)
		host = input("--> ")
		print("\n")
		port = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80, 127, 280, 281, 350, 5000, 8000, 8080]

		for i in port:

			try:

				scan = socket.socket()
				scan.settimeout(0.5)
				scan.connect((host, i))

			except socket.error:

				colorama.init()
				print(color_b + "Port -- ", i, " -- [CLOSED]")
				
			else:

				colorama.init()
				print(color_c + "Port -- ", i, " -- [OPEN]")
