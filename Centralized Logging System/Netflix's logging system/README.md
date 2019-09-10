<h1><a href="https://medium.com/netflix-techblog/scalable-logging-and-tracking-882bde0ddca2">Netflix's logging system</a></h1>
<h2>Goals</h2>
<p>
<ul>
<li>
Building a service that collects data from the users.
</li>
<li>
Has low latency </br>
(don't disturb the user while collecting the data)
</li>
<li>
Ok to compromise on consistency</br>
(the data being collected is non-critical, so we can drop the data instead of collecting each and every piece of data and giving trouble to the user)
</li>
</ul>
</p>
</br>

<h2>Scope</h2>
<p>
We are building a service that:</br>
Handles billions of requests a day.</br>
</p>
</br>

<h2>Capacity estimation</h2>
<p>
The log size from client is about 16KB</br>
Server response size is about 512bytes</br>
</p>
</br>

<h2>High Level Design Diagram</h2>
<img src = "img/HighLevelDesign.PNG" />
</br>

<h2>Detailed component design</h2>
<h3>How do we achive low latency? </h3>
<p>
As you can see in the diagram, as soon as we get the log we free up the request by sending it Ack.</br>
Also, as soon as we see some faliure case, don't do any processing, just take the log and return, process the log later in back end. </br>
</p>
</br>

<h2>Scale the system</h2>
To scale this, we can have multiple deployments of this cluster.</br>
</br>
<b>Pros of single cluster:</b></br>
Single deployment</br>
One place to manage / track </br>
</br>
<b>Pros of multiple deployment:</b></br>
No single point of faliure </br>
Can scale up/down independently, so one cluster doen't have to be dependent on another </br>
Easy to debug</br>
</br>
Something like this </br>
<a href = "https://blog.treasuredata.com/blog/2016/08/03/distributed-logging-architecture-in-the-container-era/"><img src = "img/Scalling.PNG" /></a>
