import zmq

# Create a ZMQ context
context = zmq.Context()

# Create a ZMQ REQ socket
socket = context.socket(zmq.REQ)

# Connect the socket to the server
socket.connect("tcp://localhost:5555")

# Send the request for a random URL to the server
socket.send_string("request random url")

# Wait for the response from the server
random_url = socket.recv_string()

# Print the received URL
print("Received URL:", random_url)
