<h1>To start the chat app</h1>
First double click on server </br>
Then go inside clients folder and double click on 2 client files</br>
You can add more clients by simply copy pasting code from client files into new files inside client folder</br>
When you add new client files they will show up while you select client to chat with </br>

<h1>Current workings</h1>
When you start the client you first select the friend you want to send message to.</br>
after you select the friend the client establishes connection with server </br></br>
when the connection is establisehd, the server then adds the client to a hashtable </br>
this hash table contains a list of active connected clients </br>
the key of this hash table is client name and value is conneciton details </br></br>
When a client sends a new message </br>
the server creates a new therad</br>
after the server recieves the message it sends Ack to client, acknowledging the reciept of the message </br>
then server checks in hash table to see if the given reciever has an open active connection</br>

<h3>If reciever is offline</h3>
Look at the image Receiver offline</br>
if the server fails to find the reciever in the hash table then it sends a message to client that the given reciver is offline </br>

<h3>If reciever is online</h3>
Look at the image Receiver online</br>
the server sends the message to reciever</br>
</br></br>
The server constantly pings the client to see if they are online or not</br>
The client sends a ping back when it gets pinged, this notifies my server that the client is online</br>
If the client doesn't send the ping back, the server concludes that the client is no longer online</br>
Once the client goes offline the server removes the client from the hash table of active connections.
