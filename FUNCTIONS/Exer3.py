#Exercise 3
try:
    def make_album(artist, title, tracks=0):
        album_dict = {
            'artist': artist.title(),
            'title': title.title(),
            }
        if tracks:
            album_dict['tracks'] = tracks
        return album_dict

    album = make_album('Bandang Lapis', 'Nang Dumating Ka')
    print(album)

    album = make_album('Katty Perry', 'Fireworks')
    print(album)

    album = make_album('Ali Gate', 'Moonlight')
    print(album)

    album = make_album('Skusta Clee', 'Lagi',tracks=8)
    print(album)

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')