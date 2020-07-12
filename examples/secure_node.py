import sys
import time
import getpass
sys.path.insert(0, '..')
sys.path.insert(0, '../../python-p2p-network')

from p2psecure.securenode import SecureNode

"""
Author: Maurice Snoeren
Version: 0.2 beta (use at your own risk)

This commandline application implements the secure node using the SecureNode
class. It becomes a secure node that could be connected to the network. You
can try it out be spinning of several of these nodes. You are able to send
information to one other.

python secure_node.py <host> <port>
python secure_node.py <port>
"""
host     = "127.0.0.1"
port     = 10000
key_file = "secure_node.dat"

if len(sys.argv) > 1:
    port = int(sys.argv[1])

if len(sys.argv) > 2:
    host = sys.argv[1]
    port = int(sys.argv[2])

# Start the SecureNode
node = SecureNode(host, port)

key_file_exists = False
try:
    with open(key_file, encoding="utf8") as f:
        key_file_exists = True

except FileNotFoundError:  
    None

except IOError:
    print("File " + key_file + " not accessible.")
    exit

if ( key_file_exists ):
    node.key_pair_load(key_file, getpass.getpass("What is your password to unlock the node:").encode('utf8'))
else:
    print("New node, generating a public/private identity, can take a couple of minutes...")
    node.key_pair_generate()
    password1 = getpass.getpass("Give password to lock your node securely:").strip()
    password2 = getpass.getpass("Retype your password:").strip()
    if ( password1 == password2 ):
        node.key_pair_save(key_file, password1)
        password1 = password2 = None
    else:
        print("Password do not match!")
        exit 

node.start()
node.debug = False
time.sleep(1)

running = True
while running:
    print("Commands: message, ping, discovery, status, connect, debug, stop")
    s = input("Please type a command:")

    if s == "stop":
        running = False

    elif s == "message":
        node.send_message(input("Message to send:"))

    elif s == "ping":
        node.send_ping()

    elif s == "discovery":
        node.send_discovery()

    elif s == "status":
        node.print_connections()

    elif s == "debug":
        node.debug = not node.debug

    elif ( s == "connect"):
        host = input("host: ")
        port = int(input("port: "))
        node.connect_with_node(host, port)

    else:
        print("Command not understood '" + s + "'")   

node.stop()
