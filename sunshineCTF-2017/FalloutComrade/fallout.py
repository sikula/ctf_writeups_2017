#!/usr/bin/env python
#===============================================================================
# @Author: Peter Sikula
#===============================================================================

import socket
import sys
import time

menu = """2 - fallout
3 - survivor
5 - comrade
7 - nuclear
11 - apocalypse
13 - shelter
17 - war
19 - radioactive
23 - atom
29 - bomb
31 - radiation
37 - destruction
41 - mushroom
43 - armageddon
47 - disaster
53 - pollution
59 - military
61 - science
67 - winter
71 - death
73 - atmosphere
79 - bunker
83 - soldier
89 - danger
97 - doomsday"""


table = dict([x.split(" - ") for x in menu.split("\n")])


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print "[!] Failed to initiate socket\n"
    sys.exit()
else:
    print "[+] Socket successfully created\n"

    # connect to the socket
    HOST = "pwn.sunshinectf.org"
    PORT = 30001
    sock.connect((HOST, PORT))

    # set a small timeout to ensure we recv the data
    time.sleep(1)

    # get reply from socket
    print sock.recv(2048)

    # begin the challenge
    sock.sendall("\n")


def calculate_value(data):
    result = ""

    if data in table:
        result = table[data]
    else:
        for key in sorted(table.keys(), key=int):
            if int(data) % int(key) == 0: result += table[key]

    if result == "":
        result = "FAKE NUMBER"

    return result


while True:
    time.sleep(2)
    output = sock.recv(1024).strip()
    if output == None:
        break
    else:
        print "[ reply ] {}".format(output)
        result = calculate_value(output)
        print result
        sock.send(result + "\n")
