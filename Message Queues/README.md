<h1>Message Queues</h1>

  <h2>What is it ?</h2>
  <p>It's a temporary storage system between a sender and receiver. 
  So a sender sends a message and they are done, they can then process the next message to send. 
  On the other hand, the receiver receives the message and then they can take their own time to act on it.
  </p>
  <p>One of the best example of message queue is email.
  The sender sends an email and the receiver at their own convenience opens it up and replies.
  There is no added pressure of immediately responding to it.
  </p>
  <img src="img/MessageQueues.PNG">
  
  <h2>Uses</h2>
  <ul>
      <li>Allows for asynchronous processing</li>
      <li> <b>Stream processing: </b>
      Data can be continuously streamed and processed at the same time.</li>
      <li><b>Event driven architecture: </b> 
      Can be used in publisher and subscriber model. 
      So you can write a software that listens to a bunch of events and respond to only the one's they are interested in.</li>
      <li><b>Building a fault tolerant system: </b>
      Imagine you have a distributed system, when one of it's micro-service fails, your queue can still hold the data in it.
      Once the micro-service is back up again, it can pick up the messages from the queue where it left off.
      </li>
  </ul>
  
  
  <h2>Good reads</h2>
  https://docs.microsoft.com/en-us/learn/modules/cmu-message-queues-streams/
  </br>
  https://www.freecodecamp.org/news/a-dummys-guide-to-distributed-queues-2cd358d83780/
  </br>
  
  
  