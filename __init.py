# Panic at the distro
# Author: s0nlxaftrsh0ck
# Date: 5/16/2022
# Usage: Download my favorite linux distros + other ISOs as well


# Sites to scrape from:
# https://distrowatch.com/
# Should I get ISOs direct from the sites they originated from??

# For parsing a web page
from cgitb import html
from bs4 import BeautifulSoup

# For grabbing and using the ISOs via .torrent files
import qbittorrent

# For converting / downloading the page needed for scraping
import requests

# For using system functions / read and write files
import os



page = requests.get("https://distrowatch.com")

page_content = page.text

with open('/home/s0nlx/Coding/Panic-at-the-Distro/.sites/DistroWatch-Torrent.html', 'w', encoding='utf-8') as fp:
    fp.write(page_content)

# print(page.status_code) # Received Status code 200 @ https://distrowatch.com

# print(page.content)

soup = BeautifulSoup(page_content, 'html.parser')

# print(soup.prettify())

# print(list(soup.children))

# BeautifulSoup Objects for DistroWatch
# [0] = DocType
# [1] = Tags
# [2] = NavigableString
print([type(item) for item in list(soup.children)])

# Put the tags into the html 
html = list(soup.children)[1]

print("\nTag List created\n")

# Print out URLs?
a_tag = html.a
link = a_tag['href']

print("\nPrinting out links\n")

print(link)

# Print out the tag list
#print(list(html.children))

#print("\nBody created...\n")

#body = list(html.children)[0]

#print("\nPrinting body\n")

#print(list(body.children))

#print("\nGrabbing paragraphs\n")

#p = list(body.children)[1]

#print("\nPrinting Text from paragraphs\n")

#print(p.get_text())

#print("\n--->End<---\n")

# Finding all instances of a tag at once

#all_option = soup.find_all('option')[0].get_text()

#print(all_option)