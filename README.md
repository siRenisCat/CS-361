#### REQUEST data from the microservice
1. Create a ZeroMQ context using context = zmq.Context().
2. Create a request socket using socket = context.socket(zmq.REQ).
3. Connect the socket to the server.
4. Send a request message to the server by calling the send_string method on the socket and passing in the message as a string. 
#### RECEIVE data from the microservice 
1. Wait for the response from the server using the recv_string method of the socket. 
2. Once a response is received from the server, the response is stored in a variable random_url.
#### UML sequence diagram 

<img width="409" alt="Screen Shot 2023-02-10 at 7 28 42 PM" src="https://user-images.githubusercontent.com/91215520/218226216-37df49a6-dd2d-4e69-80f7-23308b3602df.png">
