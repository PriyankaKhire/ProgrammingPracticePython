<h1>Design a video sharing service like Youtube or Netflix</h1>
<h2>Goals</h2>
1) Upload a video</br>
2) View a video</br>
</br>
3) Search for a video</br>
4) Capture stats like, comments, likes, views on a video.</br>
</br>
5) System should be highly available</br>
6) System should be hightly reliable</br>
7) System can take a hit on Consistency</br>
</br></br>

<h2>Scope</h2>
Let's design this system for multiple users.</br></br>

<h2>Capacity Estimations</h2>
Our system is read heavy. </br></br>
Let's have 5 Million active users.</br>
</br>
Let's assume that 1 user views about 5 videos per day</br>
Thus total video views 5*5 Million = 25 Million views per day.</br>
</br>
Let's assume there is 1 video uploaded per second.</br>
</br>
<b>Upload Storage Estimations</b></br>
Let's assume per minute we get about 1 hour worth of video data</br>
Let's assume the size of 1 hour of data is 1 GB</br>
Per day we'd need 60 Min* 24Hour = 1440GB</br>
</br>
<b>Upload Bandwidth Estimations</b></br>
Since we are getting 1 hour of video data per min.</br>
That is 60 mins of data per min</br>
And if we can upload 10MB per min.</br>
We'd need to upload 60*10MB = 600MB per min</br>
</br>

<h2>High Level design</h2>
<h3>Upload Video</h3>
<img src = "HighLevelUploadVid.PNG" />
</br></br>
<h3>Watch Video</h3>
<img src = "HighLevelWatchVid.PNG" />
</br></br>
<h3>Search Video</h3>
<img src = "HighLevelSearchVid.PNG" />
</br></br>

<h2>Code</h2>
<h3>Classes</h3>
<b>User</b></br>
ID</br>
UserName</br>
VidsUploaded = [List of vid ids]</br>
HistoryOfVidsWatched = [List Of Vid Ids]</br>
Subscription = [List Of User ID]</br>
</br>
<b>Video</b></br>
ID</br>
Title</br>
Description</br>
Comments = [List Of Comment Objects] </br>
Video = Location of vid file</br>
Thumbnail = Location of image</br>
UserID (user who uploaded this video) </br>
Date and time of creation </br>
Total Number of views</br>
Total number of Likes</br>
</br>
<b>Comment</b></br>
ID</br>
Text</br>
UserId (who created the comment) </br>
VidId (Where the comment was left) </br>
</br></br>
<h3>APIs</h3>
<b>UploadVid(user object, vid object, vid Content)</b></br>
vid content = the video stream</br>
Returns: Success if the video was uploaded successfully</br>
</br>
<b>WatchVid(user Object, vid url)</b></br>
Returns: Stream of vid requested</br>
</br>
<b>SearchVid(user object, search term)</b></br>
Returns: top 10 vid objects</br>
</br>
Note: instead of user object, we can send user api key.</br>
We can eliminate the hacker attacks if we send the api key. </br>
So if we decide to send the api key then APIs would look like this</br>
<b>UploadVid(apiKey, vidStream, title, description, timeStamp)</b></br>
<b>WatchVid(apiKey, vidUrl)</b></br>
<b>SearchVid(apiKey, searchTerm, [optional]VidCountToReturn)</b></br>
</br></br>

<h2>Detailed Component Design</h2>
There are 3 components to this system.</br>
<h3>Upload</h3>
<img src = "Upload.PNG" />
</br>
<h3>Watch</h3>
<img src = "Watch.PNG" />
</br>
<h3>Search</h3>
<img src = "Search.PNG" />
</br>
Reason why I have 3 different databases for user content, video content, metadata content is because there are 3 different data types here. 1) videos 2) Text/objects (for user data) 3) Image data (metadata may contain thumbnail images).</br>
So each database represents a storage system</br>
We can use different storage systems for different types of data</br>
Why are we doing this ?</br>
It’s recommended to store large static files like videos and images separately as it has better performance and is much easier to organize and scale. </br>
<h3>Database design</h3>
The service is read heavy.</br>
So we need to design a database server that can fetch content fast.</br>
For this purposes we use relational database</br>
The user to video relationship can be like this</br>
<img src = "RelationalTable.PNG" />
<b>Video storage system</b></br>
For storing the video we can store it in a distributed file storage system.</br>
Now if you are in USA and you want to watch a video that is stored in Indian database server, it will take time for that video to load.</br>
So to avoid this issue we have CDN.(content delivary network)</br>
A CDN is system if distributed servers, that are distributed over geographic locations.</br>
The CDN server will host your content on their servers. So users instead of accessing content from the main server that may be far away from them, can instead access content from a server that's near to them physically.</br>
Advantage: your content is replicated (that means it has a backup)</br>
<b>But we have a lot of data !! can we replicate all of it on CDN servers ?</b></br>
One straightforward approach is to host popular videos in CDN and less popular videos are stored in our own servers by location</br>
</br></br>

<h2>Scale the system</h2>
<h3>Sharding Metadata</h3>

