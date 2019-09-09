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
