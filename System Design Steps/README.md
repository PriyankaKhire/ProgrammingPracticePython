<h1>How to approch System design</h1>

<h2>Goals</h2>
<p>
Just what exactly am I designing here ? </br>
Who are the users, how will they use this system ?</br>
<b>What are the input and outputs of the system ? </b></br>
</p>
</br>

<h2>Scope</h2>
<p>
Am I designing this system for: </br>
<ul>
<li> 1 User </li>
<li> Multiple users </li>
<li> Billions of users </li>
</ul>
</br>
Should I discuss end to end experience or just the API ? </br>
</p>
</br>

<h2>Capacity estimation</h2>
<p>
How big of a system am I actually designing ?</br>
How much data would be produced ? </br>
How many read write requests per second ? </br>
</br>
<ul>
<content>So let's say you have 500Million monthly active users</content></br>
<content> That is 16Million users per day -> 600Thousand users per hour -> 10 Thousand users per min -> 166 users per second (These caculations may not be accurate, we are just estimating)</content></br>
<content>But this is a perfect world senario, no application in real life is perfect and no senario is perfect either</content></br>
<content>In real life traffic is unevenly distributed, so for example for an app like facebook, most people like to come home and check it. That means traffic probably increases after 5:00PM</content></br>
<content>So the question you should be instead asking is: </content></br>
<content>where are these users ?</content></br>
<content>Are these users distributed evenly geographically ? Becasuse different countries will give you different traffic patterns</content></br>
<content>How much percent of these monthly active users are actually active daily ?</content></br></br>
<content> Let's say our above calculations were correct, that there would be 10Thousand active users per min in worst case senario</content></br>
<content>And we have written a server that can handle roughly about 1000 people per min.</content></br>
<content>That means we'd need about 10 servers to handle the load at given time</content></br>
<content> So you have taken a big problem of 500Million active users and broken it down </content></br>
</ul>
On basis of all this, you can scale the system</br>
Also, don't forget about the overall consumer impact of your system.</br>
Like, you are designing a system, but will the consumer benifit from your design ? because if they don't they wont use the system</br>
</p>
</br>

<h2>High Level diagram</h2>
<p>
Draw stuff... </br>
Start with high level block diagram.</br>
</p>
</br>

<h2>Code</h2>
<p>
Design the classes </br>
<b>Design what your APIs look like ? what do they take in ? what do they return ?</b> </br>
Write some code, what algo will you use ?</br>
</p>
</br>

<h2>Define a data model</h2>
<p>
Ok, so we designed classes, but what is the primary key ? </br>
How exaclty am I storing them ? <?br>
</p>
</br>

<h2>Detailed component design</h2>
<p>
Pick a component they are interested in and go deep there. </br>
</p>
</br>

<h2>Bottleneck of the system designed so far </h2>
<p>
Before proceeding to scale the system, we look at the bottlenecks of the system designed so far and discuss that with the interviewer.
</p>
</br>

<h2>Scale the system</h2>
<p>
Time to add Load balencers </br>
Add some cache </br>
Sharding </br>
<b> Remember: You NEED to have a working system before you can scale it. </b> </br>
</p>
</br>

<h2>Tradeoffs</h2>
<p>
Don't forget to discuss tradeoffs of big systems</br>
Do this every time you bring up new things </br>
Identify bottlenecks </br>
</p>
