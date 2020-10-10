import requests
from bs4 import BeautifulSoup
songs = []

url = "https://www.openbsd.org/lyrics.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


h2s = soup.findAll('h2')

for e in h2s: 
    song = {
        "title": "",
        "mp3": "",
        "image": "",
        "info": "",
        "lyrics": ""
    }
    print (e.text)
    if e.find_next_sibling('table'):
        print ( e.find_next_sibling('table').text)
    else:
        print("No tiene table")
    input()