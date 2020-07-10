import sys
import time
sys.path.insert(0, '..')

from p2psecure.securenode import SecureNode

node1 = SecureNode("localhost", 10001)
node2 = SecureNode("localhost", 10002)

node1.start()
node2.start()
node1.debug = True
node2.debug = True
time.sleep(1)

node1.connect_with_node("localhost", 10002)

node1.send_ping()
node2.send_ping()

node1.stop()
node2.stop()

node1.join()
node2.join()

print("End")