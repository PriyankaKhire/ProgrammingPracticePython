<h1>How to Run the App</h1>
Go in the servers folder and first start Server.py then StoreMessagesDatabase.py and finally GetMessagesDatabase.py</br>
Then go inside Clients folder and start both the clients</br></br>

<h1>Current workings</h1>
<h2>Register the user</h2>
<img src="https://github.com/PriyankaKhire/ProgrammingPracticePython/blob/master/Messaging%20Service/ChatServerWithMessageStoring/Register%20User.PNG" />
<p>
    When you first start the client, it asks if you want to register or login.</br>
    If you select the Register option, it takes you to register the new user.</br>
    I suggest you register a few users before trying out the service. </br>
    During registration the script asks for First name, last name, email, and desired user name. </br>
    It then checks if you have any friends or not, since you just registered you will not have any friends</br>
    If there are no other users, the other user list will be empty. I suggest at this point you quit the script and restart it.</br>
    Now after you have registered a few users, you can then proceed to log in.
</p></br>

<h2>Login the user</h2>
<img src="https://github.com/PriyankaKhire/ProgrammingPracticePython/blob/master/Messaging%20Service/ChatServerWithMessageStoring/Login%20User.PNG" />
<p>
    Now if you select the log in option, the script checks the database and then gets the current user object.</br>
    The script then proceeds to get a receiver object by first checking the friend list of the current user object.</br>
    If the friend list is empty it then displays the list of users to add as friends</br>
    You can add users who have you in their friend list or even users who don't have you in their friend list. </br>
    After you have added a few friends ( You won't be able to add more friends later )</br>
    You can then proceed to select the user who you want to chat with.</br>
    The database then assigns this user's object to receiver</br>
</p></br>

<h2>Architecture</h2>
<img src="https://github.com/PriyankaKhire/ProgrammingPracticePython/blob/master/Messaging%20Service/ChatServerWithMessageStoring/Message%20Passing.PNG" />
<p>
    At first the client establishes the connection with server, the client sends its user's UserName to server.</br>
    The server stores this information in a hash table called "clients". </br>
    This hash table has key = user name and value = connection object. </br>
    Now the server starts a new thread for this client (Look at the ClientThread function)</br>
    The server maintains a constant connection with client by constantly pinging it. </br>
    If the server receives a ping back it keeps the connection with the client open else it closes it.</br>
    This is what is refer to as <b>Constant heartbeat ping</b></br>
</p>
<p>
    On the client side when you first start writing the message, a message object gets created.</br>
    This message object stores the text message, sender's user name, receiver’s user name, time stamp and sequence number.</br>
    (Although, I haven't really used the sequence number)</br>
    The client then sends this message object to server</br>
    On a different thread, the client is constantly looking to receive messages</br>
</p>
<p>
    On the server's side when a new connection is first established it contacts the GetMessagesDatabase server.</br>
    The server sends the sender's and receiver’s user names.</br>
    Up on receiving these user names, the GetMessagesDatabase server then tries to fetch the <b>Previous Message history of the sender</b>.</br>
    The GetMessagesDatabase server first contacts the database to get the sender's UserConversation object.</br>
</p>
<p>
    In the database the key is the user name and the value is their UserConversation object.</br>
    The UserConversation object stores the user name and their conversation history in a hash table called conversationHistory </br>
    This conversationHistory hash table has key as user name of other user (with whom our main user is having the conversation with)</br>
    and the value as a queue of messages.</br>
    The UserConversation object also has another hash table called unreadMessages.</br>
    The unreadMessages hash has key as other user's user name and value as queue of all the messages from that user which our current user didn't read.</br>
</p>
<p>
    When the GetMessagesDatabase server receives this object it gets the conversation history of the receiver from conversationHistory hash.</br>
    Then it gets the unread messages sent by the receiver to our sender from the unreadMessages hash.</br>
    The GetMessagesDatabase server then appends these 2 queues the following way = [conversation history] + [unread messages] </br>
    GetMessagesDatabase server then deletes the receiver’s entry from the unreadMessages hash and stores this newly formed queue into conversation history</br>
    This edited UserConversation object is then stored back in database.</br>
    Now if the sender didn't have any unread messages from the receiver then conversation history remains as is. </br>
    It then selects the recent 10 messages from the conversation history queue.</br>
    And sends these messages one by one to server</br>
    The server passes these messages to the sender. </br>
    Thus on the sender's screen we see the unread messages plus the previous conversation history.</br>
    If there is no conversation history between the users, no messages are sent</br>
</p>
<p>
    Now when the server receives the message, it sends an "Ack" back to the sender.</br>
    It extracts the receiver of this message from the message object and then checks in client's hash table if this receiver has opened any connection with the server or not.</br>
    If the receiver is not found in the client's hash then server sends a message to sender notifying that the receiver is not online. </br>
    If the receiver is found in the client's hash then the server passes the message to the receiver.</br>
    What I would have liked that once the reciever gets the message it sends an "Ack" to server and then server sends "Message Delivered" notification to sender. But I became impatient to add this feature.</br>
</p>
<p>
    Weather receiver is offline or online the server passes these messages and delivary status of the receiver to StoreMessagesDatabase server to <b>store the message history</b>.</br>
    The delivary status of the receiver can be either 'read' or 'unread' for the sender however this status is always 'read'.</br>
    Now this is the database that could have used the sequence numbers, it could have appended the messages in right order and saved, but I became impatient to add that feature.</br>
    Also it is worth mentioning that this database is not multithreaded, so the order of messages can be different when you see the recent messages</br>
    When StoreMessagesDatabase server receives the delivary status of receiver and the message object, it first gets the sender's and receiver's UserConversation objects from the database.</br>
    The StoreMessagesDatabase server stores the message from sender in sender's read conversation history, the message is stored in following way:</br>
    In the UserConversation object of the sender there is a conversationHistory hash, the server finds the reciever's key and gets the messages queue, the current message is appended to the end of this queue</br>
    Similarly for the reciever, depending on the delivary status the message is either stored in conversationHistory hahs or unreadMessages hash, here we find the entry in the hash pertaining to sender.</br>
    After this the database is updated with the sender's and receiver's UserConversation objects</br>
</p>

