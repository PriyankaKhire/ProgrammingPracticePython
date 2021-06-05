<h1>HTTP Request</h1>
  <p>HTTP (Hypertext Transfer Protocol), is the underlying format that is used to structure request and responses between a client and a server.</p>
  <img src="img/HTTP.png">
  <p>The client (your computer) opens a TCP (Transmission Control Protocol) channel with the server it wants to communicate to. HTTP is the command language that the devices on both sides of the connection must follow in order to communicate. <br/>After the server sends the response it closes the TCP connection.</p>
  <img src="img/TCP.png">
  
  <h2>HTTP vs HTTPS</h2>
    <p>HTTPS stands for HTTP secure, it encrypts the data you send to server. Thus it’s more secure.</p>
  
  <h2>Popular Types of HTTP Request Methods</h2>
    <h3>GET</h3>
      <p>Client sends a GET request to the server to get the requested contents from it. </p>
    <h3>POST</h3>
      <p>Used to send data to a server to create/update a resource, these requests are NOT idempotent.</p>
      <p>So if you retry the request N times, you will end up having N resources with N different URIs created on server.</p>
      <p>Example: User uploading a profile picture.</p>
    <h3>PUT</h3>
      <p>PUT requests are same as POST requests, except for they are idempotent.</p>
      <p>So if you send retry a request multiple times, that should be equivalent to single request modification.</p>
      <p>Example: Adding caption under the profile picture.</p>
    
    
  
  

  
  
  