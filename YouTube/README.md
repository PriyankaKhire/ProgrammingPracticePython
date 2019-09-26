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
</br></br>

<h2>High Level design</h2>
<h3>Upload Video</h3>
<img src = "" />
</br></br>
<h3>View Video</h3>
<img src = "" />
</br></br>
<h3>Search Video</h3>
<img src = "" />
</br></br>
