
from bs4 import BeautifulSoup
import re

baseURI = "http://127.0.0.1:3000/.sites/"
# baseURI = "https://distrowatch.com/" # This is for the prod script

dlPage = open('.sites/DistroWatch-Torrent.html','r')
soup = BeautifulSoup(dlPage, "html.parser")

# SP1 Found Torrent links

tList = soup.find_all('td', class_="torrent") 

print(tList)

# SP2 = Spitting things out into an organized list or array....
# Weird snag - Shift + Enter doesn't execute the python file anymore?
#       - Seems to be due to Environment Variables updating with VSCode updates...

#for i in soup.find_all('a', {'href':re.compile("(?<=<a href=\").*.torrent(?=\")")}):
#    print(i) 




# Save Point 1: Trying to find the tag to the torrent links
# with BeautifulSoup, torrent links are under the <td></td> tag
# But can't seem to print out that link
# Then try to send the link to qBitorrent to download


# Save Point 2: Trying to find the nested <a href=...
# Find the title of it a specific distro "Ubuntu" and it's corresponding
# Torrent URI send that link to qBitorrent
# [X] Can I just grab the links from the XML?
#   | https://distrowatch.com/news/torrents.xml
# Nope. XML file isn't the full list of torrents...
# But could probably keep an eye on the RSS feed to get up to date downloads
# All links have the same pre-fix however
# Base URI: https://distrowatch.com/dwres/torrents or locally http://127.0.0.1:3000/.sites/
# Target URI: /3cx-debian-amd64-netinst.iso.torrent
# Combining it https://distrowatch.com/dwres/torrents/3cx-debian-amd64-netinst.iso.torrent or baseURI+targetURI
# .News1 > blockquote:nth-child(1) > table:nth-child(10) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3)
# ^^^ This seems to be what I need BeautifulSoup to look at to get the torrent links
#   | Michael Kang found the regex for this (?<=<a href=\").*.torrent(?=\")
#       <a href="|--> 4mlinux <--|"><img find and highlight this particular tag.
#           | Found the regex for finding the source name for that torrent --> (?<=<a href=\").*(?=\"><img)
#               | Combining both (?<=<a href=\").*.torrent(?=\")|(?<=<a href=\").*(?=\"><img)