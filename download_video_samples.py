from bs4 import BeautifulSoup
import re
import requests

def direct_download(url, filename):
    res = requests.get(url, 'stream=True')
    with open(filename, 'wb') as fd:
        for chunk in res.iter_content(chunk_size=128):
            fd.write(chunk)


pattern = re.compile("http://mirrors.standaloneinstaller.com/video-sample/(.*\.(3pg|avi|flv|m4v|mkv|mov|mp4|mpeg|mpg|mts|vob|webm|wmv|))$")

html = requests.get('http://standaloneinstaller.com/blog/big-list-of-sample-videos-for-testers-124.html').text

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all('a')
for link in links:
    href = link['href']
    match = pattern.match(href)
    if match:
        filename = match.group(1)
        url = match.group(0)
        print(url, filename)
        if filename and url:
            direct_download(url, "./samples/" + filename)

