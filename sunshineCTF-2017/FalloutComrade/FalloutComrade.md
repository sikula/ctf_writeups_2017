## FalloutComrade

When you first connect to the socket, you will be greated with a menu in the form `number - string`.  You will quickly notice that the numbers are all prime numbers (this is important for the solution later).

When you begin, you will be givin a number and you need to determine if the number is real or fake. Real numbers are on the list, fake numbers are not.  But there is an added twist, numbers past 97 could be real or fake, so how do we determine which they are, and more importantly how do we determine what to send back to the socket?

This challenge was a particularly interesting challenge as it took my a long time to figure out what we needed to send back. It took me a couple hours to figure out you need find the divisors of the value and append the equivalent strings and send that to the socket.

For example:
```
6 [2 * 3]     => falloutsurvivor
8 [2 * 2 * 2] => survivor
```

After discovering that, it was a matter of creating a `Python` program to interact with the socket and send the correct values.


** The Script **

As I mentioned earlier, it was important to realize that the numbers were prime numbers.  The reason for this is that we can take the given value and determine the prime factors of that number and use that to determine the correct string to send.

For example:
```bash
6 % 2 = 0
6 % 3 = 0
```

so we know 2 and 3 are factors of 6, so we need to send  -> `falloutsurvivor`

The rest of the script is a matter of connecting to the socket and sending the correct data.

```python

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

# convert the array of form [['number', 'string']] to a dictionary {"number": "string"}
table = dict([x.split(" - ") for x in menu.split("\n")])

# create the socket connection and connect to it
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


# constructs the proper input to send to the socket
def calculate_value(data):
    result = ""

    if data in table:
        result = table[data]
    else:
        # we need to sort the keys to make sure we get the correct order
        # Example:
        #
        # falloutsurvivor and not survivorfallout
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

```

After running the script, you should get the flag!


```bash
=> flag

sun{I_g1vE_u_nUM3r0_u_G1v3_m3_alt3Rn4TE_nUMEr0}
```
