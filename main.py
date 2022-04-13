#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog
import subprocess
import time
import socket


hostname = socket.gethostname() 

IPAddr = socket.gethostbyname(hostname)

root = tk.Tk()

root.withdraw()

file_path = filedialog.askdirectory()


print("Please wait.........")

print("")

time.sleep(1)

cmd = subprocess.Popen(["python3", "-m" "http.server"], cwd=file_path, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

print("Started Server on http://{}:8000  Press Ctrl + C to exit".format(IPAddr))

print("")

print("")

print("")

try:
	while True:

		print(cmd.stdout.readline().decode())

except KeyboardInterrupt:

	print("exit")



cmd.terminate()

print(cmd.communicate()[0].decode())

time.sleep(1)

if cmd.poll() is not None:

    print('Bye for now © Cytro')

    cmd.kill()
