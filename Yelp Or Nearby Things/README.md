<h1>Design Yelp or nearby things</h1>
</br>

<h2>Goals</h2>
<ol>
<li>
Given location of the user return the top 10 "things" aroung the user.</br>
For simplicity, things = restaurants.</br>
</li>
<li>
The restaurants should be within 2 mile radius of the user.
</li>
<li>
The users should be able to add/delete/update the restaurant information.
</li>
<li>
The users should be able to add comments/feedback/review about the restaurant.
</li>
<li>
The result should have minimul latency.
</li>
</ol>
</br>
<b>Too long didn't read:</b>
</br>
<u>Input:</u> User location in latitude and longitude
</br>
<u>Output:</u> Top 10 restaurents around user within 2 mile radius.
</br></br>

<h2>Scope</h2>
For now let's design this for one user.</br>
We are assuming that the restaurent data is already populated.</br>
</br></br>

<h2>High Level Diagram</h2>
<h3>Search restaurant</h3>
<img src = "img/HighLevelDiagram.PNG" />
</br></br>

<h2>Code</h2>
<h3>API</h3>
<b>Search(user object, latitude, longitude)</b>
</br>
Returns: Top 10 Restaurant objects.
</br>
The mobile client can then render these objects into list that the user can add comment/feedback to.
</br></br>
<h3>Classes</h3>
<img src = "img/UserClass.PNG" />
<img src = "img/RestaurantClass.PNG" />
<img src = "img/CommentClass.PNG" />
</br></br>

<h2>Detailed component design</h2>
The main crux of the problem is, how do we store this data and how do we retrieve it.</br>
<h3>Trees</h3>
<img src = "img/Tree.PNG" />
You can store the world map in a tree like structure like R-Tree, Quad tree.
I am gonna be discussing about quad trees here.</br>
<b>Quad Tree</b>
</br>
You take the globe and divide it into 4 quadrants.</br>
Then you further take each quadrant and divide it into 4 more quadrants. </br>
So densely populated areas will have more rectangles on it, and sparsely populated areas will have less rectangels over it.</br>
</br>
For simplicity let's assume the most desely populated area has grid size of 2 miles by 2 miles.</br>
Further more, the leaf nodes can be connected so we can easily search over large areas.</br>
So for below use case:</br>
<img src = "img/EdgeCase.PNG" /></br>
Since the leafes are connected all we'd need to do is fetch the appropriate result from each leaf node.</br>
<img src = "img/QuadTree.PNG" />
The leaf nodes have the Ids of the restaurants contained within that grid locaiton.</br>
So when the user requests for the information, we can query the resulting leaf nodes, get the restaurents and perform the K nearest point algo on those restaurents to get our top 10 list.</br>
<b>Insert</b></br>
So to insert a restaurant, we find the appropriate leaf node and add the restaurant ID in it.</br>
Let's say the max capacity a leaf can hold is 200 restaurant Ids and we reach that, then we split the leaf node into 4 quadrants and put appropriate restaurents in each new leaf.</br>
</br>
With this approch both insert and search would be log(n) time.
</br></br>
<img src = "img/DetailedDesign1.PNG" />
</br></br>

<h2>Scale the system</h2>
<h3>Sharding</h3>
What if the entire quad tree cannot fit in memory?</br>
</br>
<h4>Region Based Sharding</h4>
<img src = "img/RegionBasedSharding.PNG" />
<b>Drawbacks:</b> </br>
What if one region becomes hot ? </br>
What if one region contains more data than other ? </br>
</br>
<h4>Grid Id based sharding</h4>
We can fit grids on the database, instead of specific location.</br>
</br>
Both the sharding approches are similar, but with grid id we are fitting the quadrants on database instead of city or state.</br>
</br></br>
<h3>Data Replication</h3>
We can have master slave architecture to ensure availability.</br>
<b>Reads:</b> The reads can be done from the master.</br>
<b>Writes:</b> The writes can be done to one of the slave, and after some time period we can make this slave the master, so other slaves can copy data off of this new master.</br>
</br></br>
<h3>Cache</h3>
To deal with hot Places, we can introduce a cache in front of our database.
</br></br>
<h3>Load Balencing</h3>
We can add Load Balencer in following 2 places: </br>
1) Between Clients and Application servers</br>
2) Between Application servers and Dababase server.
