import zmq
import random

# Load the URLs from the text file
with open("url.txt", "r") as file:
  urls = file.readlines()
  urls = [url.strip() for url in urls]

# Create a ZMQ context
context = zmq.Context()

# Create a ZMQ REP socket
socket = context.socket(zmq.REP)

# Bind the socket to a port
socket.bind("tcp://*:5555")

# Get the bound address
address = socket.getsockopt_string(zmq.LAST_ENDPOINT)

# Print the bound address
print(f"Server is listening on {address}")


while True:
  # Wait for a request from a client
  request = socket.recv_string()

  # Check if the request is for a random URL
  if request == "request random url":
    # Choose a random URL from the list
    random_url = random.choice(urls)

    # Send the URL back to the client
    socket.send_string(random_url)
