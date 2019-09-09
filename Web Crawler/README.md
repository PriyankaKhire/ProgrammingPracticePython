<h1>Design a web crawler</h1>

<h2>Use Case</h2>
<ul>
<li>Given a URL your application crawls it</li>
<ul>
<li>What do you mean by crawling ?</li>
<content> The crawler goes to each and every link on a given page and collects all links on that page. </content>
</ul>
</br>

<li>Reverse indexes pages based on key words</li>
<ul>
<li> What is reverse indexing ?</li>
<content>
When the crawler is going through the webpage, it gets the keywords on that page, and then stores them.</br>
These key words are then used to find pages on the site when user performs a search.
</content>
</ul>
</br>

<li>Generate title of the page and a small snippet of the page.</li>
<content>
Something like this.</br>
<img src="img/TitleAndSnippet.PNG" />
</content>
</br>

<li>User searches a search term, gets a list of pages containing that search term</li>
</br>

<li>The system needs to be higly available.</li>
</ul>
</br>

    <h2>Constraints</h2>
    <ul>
        <li>Traffic is not evenly distributed</li>
        <content>May have some popular searches</content>
        </br>

        <li>Need to have low latency</li>
        <content>Can we compromise on consistency ?</content>
        </br>

        <li>Need to detect cycles</li>
        </br>

        <li>Pages need to be crawled regularly to ensure freshness</li>
        <content>On an average 1ce per week</content>
    </ul>
    </br>

    <h2>Scale</h2>
    <ul>
        <li>1 billion links to crawl</li>
        </br>

        <li>100 billion searches per month</li>
    </ul>
    </br>

    <h2>High Level design</h2>
    <img src="img/HighLevelArchitecture.PNG" />
    </br>

    <h2>Indivudial component design</h2>
    <h3>Web crawler</h3>
    <img src="img/WebCrawler Component.PNG" />

    <h3>Class Design</h3>
    <pre><code>
        class Page(object):
            def __init__(self, url, title):
                self.title = title
                self.url = url
                self.timeStamp = DateTime.now()
                self.childUrls = []
        </code></pre>

    <h2>Determining when to update the crawl results</h2>
    <p>We can have another micro service that perodically updates all the crawled pages thus updating timeStamp.</br>
    This service can update both pages and indexes database.
    </p>
    </br>

    <h2>User inputs a search term and sees a list of relevant pages with titles and snippets</h2>
    <img src="img/ClientServerInteraction.PNG" />
    </br>
