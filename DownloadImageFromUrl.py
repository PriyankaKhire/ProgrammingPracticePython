#Download image from url
import urllib

def downloadImage(url):
    fileName = url.split("/")[-1]
    urllib.urlretrieve(url, fileName)

downloadImage("https://greatatmosphere.files.wordpress.com/2013/02/great-atmosphere-149-tenaya-lake-yosemite-national-park-2.jpg")
print "Completed downloading image"
