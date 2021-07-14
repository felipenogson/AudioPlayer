import requests
from bs4 import BeautifulSoup
songs = []

url = "https://www.openbsd.org/"
r = requests.get(url+"lyrics.html")
soup = BeautifulSoup(r.text, 'html.parser')


h2s = soup.findAll('h2')

for e in h2s: 
    song = {
        "version": "",
        "title": "",
        "mp3": "",
        "image": "",
        "info": "",
        "lyrics": ""
    }
    table = e.find_next_sibling('table')
    if table:
        if len(e.text.split(":")) == 2:
            song["version"], song["title"] = e.text.split(":")
            song['mp3'] = table.td.a['href']
            if table.select('td.art'): 
                song['image'] = url + table.select('td.art')[0].img['src'] 
            if table.select('td.lyrics'):
                song['lyrics'] = table.select('td.lyrics')[0].text.strip()
            if table.select('div.commentary'):
                song['info'] = table.select('div.commentary')[0].text.strip()
                print(song['info'])
            songs.append(song)
        else:
            version = "5.1"
            title = e.text.strip()
    else:
        print(e.text)
        print("No tiene table")
        
        
