<h1>Polling</h1>
  <p>Polling is the process where the client (web browser), makes an HTTP request to the server, which sends back the appropriate response.</p>
  <h2>Short Polling</h2>
    <ol>
      <li>The client opens a TCP tunnel and sends a HTTP request to the server requesting information.</li>
      <li>The server, if it has any information sends it back.</li>
      <li>The client then waits for some time and repeats the above two steps again.</li>
    </ol>
    <p>The problem with Polling is that the client has to keep asking the server for any new data. As a result, a lot of responses are empty, creating HTTP overhead.</p>
    <img src="img/ShortPolling.png">
  <h2>Long Polling</h2>
    <ol>
      <li>The client opens a TCP tunnel and sends a HTTP request to the server requesting information.</li>
      <li>The server waits until there is new information available and then sends the response back.</li>
      <li>After receiving the information the client immediately makes another request and repeats the above two steps.</li>
      <li>If the server doesn’t have any new data and the long polling request times out, then the client has to make another request.</li>
    </ol>
    <p>The server has to handle the case where it gets new information to send, but the client hasn’t sent a new request yet.</p>
    <img src="img/LongPolling.png">
  
  