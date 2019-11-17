import urllib.request
import xml.dom.minidom
from xml.dom import minidom
from xml.dom.minidom import getDOMImplementation
from xml.dom.minidom import parse, parseString
content=urllib.request.urlopen("https://www.cbsnews.com/latest/rss/main")
xmldoc = minidom.parse(content)
for element in xmldoc.getElementsByTagName('title'):
    print (element.firstChild.nodeValue)
for line in content:
    s = line.decode('utf-8')
    print(s)
content.close()

f = open('stories.html','w')
message = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>Top Stories</title>
</head>
<body>

<h2>Top Stories of the day...</h2>
<h3>by Allen Benusa</h3>
CNN.com - RSS Channel - Mobile App Manual <br />
FBI unlikely to finish review of new emails before election<br />
CLinton campaign accuses FBI of 'blatant double standards<br />
Audio of Trump praising the Clintons and Democrats<br />
Iraqi PM vows to 'chop the head of the snale' in Mosul <br />
Secret film showa rare glimpse inside Mosul<br />
Did Trump vote for George W. Bush?<br />
Kasich votes McCain instead of Trump<br />
Toddler who went viral lands modelling gig<br />
</body>
</html>
"""
f.write(message)
f.close()