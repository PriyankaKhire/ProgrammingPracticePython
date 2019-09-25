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
Create a news feed that consists of top tweets from the users our current user follows.
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
