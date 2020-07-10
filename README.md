# python-p2p-secure-node
A concrete implementation of the class Node of the p2pnetwork library. This class implement a decentralised peer-to-peer network that securely communicates between the nodes. The data is hashed and signed, so it can be checked by the other nodes. Note that the data is not encrypted. If that is needed, all the functionality is within the class methods. It is easily to extend the class. The data is in the form of dict and is send in the JSON format between the nodes.

# Secure communication
Every node creates a RSA private and public key. The node exchanges the public key with the network. Each message that is send is hashed and signed by the private key. During reception, the message is decodes and checked whether the hash is correct and the signature. Only when the message integrity passes the test, it will be handled by the node.

# Work in progress..
This class is a concrete implementation of the node class and communicates with JSON between the nodes. 
It implements a secure communication between the nodes. Not that the communication is encrypted, but
more on the tampering aspect. Messages are checked on the integrity (due to signing). A public/private
RSA key infrastructure is used to implement this. Furthermore, it implements a basic ping/pong system and
discovery. Using this node, you are able to implement your own protocol on top. All messages that are send
(make sure you use create_message method) are signed and checked when received.

# p2pnetwork
Check out p2pnetwork: https://github.com/macsnoeren/python-p2p-network. It gives you a simple framework that enables you to implement your own decentralized peer-to-peer network application in Python.