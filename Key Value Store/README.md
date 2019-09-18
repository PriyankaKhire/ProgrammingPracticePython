<h1>Key Value Store </h1>
<b>What is a key value store ?</b></br>
The most simple answer is Hash Table. </br>
<b>Drawbacks:</b></br>
What if the data is too big and cannot fit in memory ? </br>
<b>Answer:</b></br>
Distributed key value storage system.
</br></br>

<h2>Goals</h2>
Design a distributed key value sotrage system.</br>
Take in a key and return value. </br>
Make sure your system is:</br>
1) Highly available, and </br>
2) Consistant </br>
</br>
<b>Questions to ask the interviewer:</b></br>
<ol>
<li>
What type of data am I storing here ?
<ol>
<li>What data type is the key and what data type is the value ?</li>
</ol>
</li>
<li>How much data am I storing ?</li>
<li>How frequently will the data be accessed ?</li>
<li>Is the traffic evenly distributed ? </li>
<li><u>Is this a read or a write heavy system ?</u></li>
</ol>
</br></br>

<h2>Scope</h2>
How many people will be using it ?</br>
1 Million
</br></br>

<h2>Capacity Estimations</h2>
How many requests per second at worst time ?</br>
1 request per second.
</br></br>

<h2>High Level Design</h2>
<img src = "img/HighLevelDiagram.PNG" />
</br></br>

<h2>Detailed Component Design</h2>
When you say distributed key value store, it means the data is distributed.</br>
</br>
<b>Question:</b> How do you store distributed data ?</br>
<b>Answer:</b> Sharding </br>
</br>
<h3>Sharding</h3>
<b>Rule:</b> We need even distribution of data.
</br></br>
<ol>
<li>Range Based partitioning</br>
Store all the data starting from letter A on one shard etc.</br>
<b>Cons:</b> </br>
Produces inconsistency, one shard can grow bigger than another. </br>
What if one shard becomes hot ? </br>
</li>
<li>
ID/Hash-Key Based Partitioning</br>
Run the key through some sort of hash function, this gets you some id </br>
Based on this ID we can store the values.</br>
<img src = "img/HashBasedPartitioning.PNG" />
</li>
</ol>
</br></br>

<h2>Scale the system</h2>
<h3>System availability</h3>
<img src = "img/MasterSlave.PNG" /></br>
Master can have latest and slaves can copy from master.</br>
If master goes down, one of the slaves becomes the new master.</br>
</br></br>
<h3>Consistency</h3>
The reads can be done from master. </br>
The writes can be done to one of the slaves. </br>
Then after some time period, we make this most updated slave the new master.</br>
And the original master now becomes the slave.</br>
The master slave architecture should be such that the slaves continuously copy off the master, so when we change the master, the slaves should be now copying off the new master. Thus making them also updated.</br>
This approch will compromise the latency of the most consistent data.</br>
</br></br>
<h3>Cache</h3>
We can put the most accessed data in LRU cache on the server.
</br></br>
<h3>Cluster</h3>
As the data grows and the customers grow, we'd eventually need to split the architecture into multiple clusters. </br>
We can use consistent hashing to add or remove the servers. </br>
Since we have decided to shard based on hashId, and if we decide to add more servers, this approch of load balencing would make sense</br>
