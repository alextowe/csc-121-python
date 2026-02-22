def make_album(artist, title, songs=None):
    album = {"artist": artist.title(), "title": title.title()}
    if songs:
        album["songs"] = songs
    return album

album = make_album("remember that you will die", "polyphia")
print(album)

album = make_album("master of puppets", "metallica")
print(album)

album = make_album("the dark side of the moon", "pink floyd")
print(album)

album = make_album("the wall", "pink floyd", songs=26)
print(album)

while True:
    print("\nPlease tell me the album information:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Album Title: ")
    if title == 'q':
        break

    songs = input("Number of Songs (optional): ")
    if songs == 'q':
        break
    elif songs.isdigit():
        songs = int(songs)
    else:
        songs = None

    album_info = make_album(artist, title, songs)
    print(album_info)