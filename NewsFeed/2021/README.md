<h1>News Feed</h1>
    <h2>Requirements</h2>
        <ol>
            <li>Generate News Feed based on people a user follows</li>
            <li>A user may have many friends</li>
            <li>Feeds may contain videos, images, text</li>
            <li>When new post arrives, append it to the user's timeline</li>
            <li>We need a fast system, so low latency</li>
        </ol>
    <h2>Scope: Multi User, Probably 10 Users</h2>
    <h3>Class Design</h3>
        <p>
        <b>User Class</b> { <br/>
        Name: String <br/>
        Id: int <br/>
        email: String <br/>
        Friends: [List of user Ids] <br/>
        Posts: [List of Post Objects] <br/>
        }
        </p>
        <p>
        <b>Post Class</b> { <br/>
        Id: int <br/>
        timestamp: Date <br/>
        Content: String <br/>
        Img attachemtns: Storage Url <br/>
        Videos: storage url <br/>
        }
        </p>
    <h3>API Design</h3>
        <p>
        <b>Get_Latest_User_Posts</b>(UserId, number of posts)
        </p>
        <p>
        <b>Generate_newsfeed</b>(userId, Number of posts, How many hours of data)
        </p>
        <p>
        <b>Post_Content</b>(UserId, PostObject)
        </p>
    <h2>Scope: 100,000 Users</h2>
    <h3>High Level Diagram</h3>
    <img src="img/SavingPostHighLevelDiagram.PNG">
    <br/>
    <img src="img/GeneratingNewsFeedHighLevel.PNG">
    
    
    
    