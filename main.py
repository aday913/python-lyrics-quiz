import lyricsgenius as lg

api_key = "<InsertAPITokenHere"

genius = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True
)

artist = genius.search_artist("ArtistNameHere", max_songs=5, sort="popularity")

songs = artist.songs
print([i.title for i in songs])
