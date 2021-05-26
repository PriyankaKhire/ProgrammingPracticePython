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
    <h3><span style="color:blue">Multi User, Probably 10 Users</span></h3>
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
    
    
    