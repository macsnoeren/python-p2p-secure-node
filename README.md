# python-p2p-secure-node
Implementation of a secure node based on the python p2pnetwork framework.

# Work in progress..
This class is a concrete implementation of the node class and communicates with JSON between the nodes. 
It implements a secure communication between the nodes. Not that the communication is encrypted, but
more on the tampering aspect. Messages are checked on the integrity (due to signing). A public/private
RSA key infrastructure is used to implement this. Furthermore, it implements a basic ping/pong system and
discovery. Using this node, you are able to implement your own protocol on top. All messages that are send
(make sure you use create_message method) are signed and checked when received.

# p2pnetwork
Check out p2pnetwork. It gives you a simple framework that enables you to implement your own decentralized
peer-to-peer network. The SecureNode class uses this framework to implement a specific application. p2pnetwork
provides a "bare" implementation, so you can make all the application specific functionality yourself!