<h1>News Feed</h1>
    <h2>Requirements</h2>
        <ol>
            <li>Generate News Feed based on people a user follows</li>
            <li>A user may have many friends</li>
            <li>Feeds may contain videos, images, text</li>
            <li>When new post arrives, append it to the user's timeline</li>
            <li>We need a fast system, so low latency</li>
        </ol>
    <h2>Scope of the system</h2>
    <h3>Multi User, Probably 10 Users</h3>
    <h4>Class Design</h4>
        <p>
        <b>User Class</b> { <br/>
        Name: String <br/>
        Id: int <br/>
        email: String <br/>
        Friends: [List of user Ids] <br/>
        Posts: [List of Post Objects] <br/>
        }
        </p>
        <br/>
        <p>
        <b>Post Class</b> { <br/>
        Id: int <br/>
        timestamp: Date <br/>
        Content: String <br/>
        Img attachemtns: Storage Url <br/>
        Videos: storage url <br/>
        }
        </p>
    <h4>API Design</h4>
        <p>
        <b>Get_Latest_User_Posts</b>(UserId, number of posts)
        </p>
        <p>
        <b>Generate_newsfeed</b>(userId, Number of posts, How many hours of data)
        </p>
        <p>
        <b>Post_Content</b>(UserId, PostObject)
        </p>
    
    
    
    