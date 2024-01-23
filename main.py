import os

import lyricsgenius as lg
from dotenv import load_dotenv

load_dotenv()

api_key = f"{os.getenv('GENIUSACCESSTOKEN')}"

genius = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
    timeout=10
)

artist = genius.search_artist("Metallica", max_songs=5, sort="popularity")

songs = artist.songs
print([i.title for i in songs])

# Now we can try to get a particular song using the sdk:

song = genius.search_song(title='One', artist='Metallica')
print(song.title)
print(song.artist)
