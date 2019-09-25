<h1>Design Twitter</h1>
<h2>Goals</h2>
<ol>
<li>
User should be able to:
<ol>
<li>Post a new tweet</li>
<li>Follow other users.</li>
<li>Like a tweet</li>
</ol>
</li>
<li>
Create a Time Line for:
<ol>
<li> Home Time Line/ News Feed: That consists of top tweets from the users our current user follows.</li>
<li> User Time Line: That consist of top recent tweets our user has made</li>
<li> Search Time Line: That consists of tweets based on a search term</li>
</ol>
</li>
<li>
The system needs to be:
<ol>
<li>Highly available</li>
<li>Can have some latency</li>
<li>Can take a hit on consistency</li>
</ol>
</li>
</ol>
</br></br>

<h2>Scope</h2>
Let's first desgin a system for 1 user for now.
</br></br>

<h2>Capacity Estimations</h2>
Let's have some assumptions</br>
100 Million total Users</br>
200,000 active users</br>
100,000 tweets per day</br>
On average 1 user follows 200 other users</br>
</br>
<b>Liked tweets</b></br>
1 user likes 5 tweets per day</br>
200,000 users will like 10,00,000 tweets per day.
</br></br>
<b>Tweet Views</b></br>
Let's say the timeline of any user has at max 10 tweets.</br>
Our current user visits their timeline 2ce a day and also visits 5 other people's timelines</br>
So total timelines the current user sees is 7</br>
And as stated above that each timeline consists of about 10 tweets</br>
So total tweets = 70</br>
And we have about 200,000 active users</br>
So total tweet views is 200,000*70 = 140,000,000 </br>
</br>
<h3>Storage Estimations</h3>
What does our tweet consist of ?</br>
1) Text (max 140 chars)</br>
2) Image/video </br>
3) other metadata like timestamp, tweet id etc.</br>
<b>Pure Text tweet without Image/Video</b></br>
Let's say we need about 300 bytes to store the text</br>
And about 50 bytes to store metadata.</br>
So 1 pure text tweet size is: 300 bytes + 50 bytes = 350Bytes</br>
<b>Text+Image tweet</b></br>
Let's say we need about 300 bytes to store the text</br>
And about 50 bytes to store metadata.</br>
And 200KB to store the image</br>
So 1 Text+Image tweet size is: 300 bytes + 50 bytes + 200KB = 200.35KB</br>
<b>Text+Video tweet</b></br>
Let's say we need about 300 bytes to store the text</br>
And about 50 bytes to store metadata.</br>
And 2MB to store the video</br>
So 1 Text+Image tweet size is: 300 bytes + 50 bytes + 2MB = 2.00035MB</br>
<b>Total Storage Per Day</b></br>
Let's say we have 20% tweets that contain Images and 10% tweets contain Videos</br>
So out of 100,000 we have 20,000 tweets with images and 10,000 tweets with videos and rest 70,000 pure text tweets.</br>
Total storage required would be:</br>
70,000*350Bytes+20,000*200.35KB+10,000*2.00035MB = 24.03500 GB </br>
</br>
<h3>Bandwidth Estimations</h3>
So if 24GB per day then 24GB/24Hours = 1GB per hour, 1GB/60Mins*60Seconds per second
</br></br>

<h2>High Level Design</h2>
<h3>Post Tweet</h3>
<img src = "HighLevelDesign.PNG" />
</br></br>
<h3>Get News Feed</h3>
<img src = "HighLevelDesign2.PNG" />
</br></br>
<h3>General system analysis</h3>
We saw from Capacity Estimations we get 100,000 tweet writes per day but 140,000,000 tweet views per day.</br>
So our system is <u>READ HEAVY</u> </br>
</br></br>

<h2>Code</h2>
<h3>Classes</h3>
<b>Tweet</b></br>
UserId (who created the tweet)</br>
TweetID</br>
Text</br>
Image</br>
Video</br>
TimeStamp</br>
FavouritedBy = [List of UserID] (users that have marked this tweet as their favourite)</br>
</br>
<b>User</b></br>
ID</br>
UserName</br>
Follows = [List of UserIDs]</br>
FavouriteTweets = [List of TweetIDs]</br>
</br></br>
<h3>API</h3>
<b>CreateTweet(UserId, Text, [Optional]Image, [Optional]Video)</b> </br>
Creates a tweet object</br>
Returns success if a tweet object is created successfully</br>
<b>PostTweet(TweetObject)</b></br>
Returns success if the tweet is posted successfully</br>
</br></br>

<h2>Detailed Component Design</h2>
<h3>Post Tweet</h3>
<img src = "UserRelationshipTable.PNG" />
Generally the user has 1:Many relationship, when it comes to tweets and followers.</br>
The above tables explain this.</br>
<img src = "PostTweet.PNG" />
<b>Redis Database</b>: Redis is in memory database, it has key value pairs kinda like hash table. It offers data replication.</br>
So in our above diagram the data is replicated 3 times in the Redis cluster </br>
It is very easy to insert huge amounts of data easily</br>
</br>
<b>Bottleneck of the above approch</b></br>
Every time the user tweets the data is getting replicated 3 times, so what about hot users like celebs ? </br>
To solve this problem, we can merge celeb tweets at load time of timeline.</br>
So every time user tweets, all their follower's time line gets pre computed.</br>
When the follower accesses their time line, during the access time, if the follower is following celeb that time the tweet is loaded.</br>
<img src = "GetTimeLine.PNG" />
