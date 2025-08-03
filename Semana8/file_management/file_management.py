list_of_songs_file = "metal_playlist.txt"
path = f"{list_of_songs_file}"


def sortPlaylist(path, songs_file):

    new_song_list = []

    with open(path, "r", encoding="utf-8") as songs_file:

        for song in songs_file:
            print(song)
            formatted_text_song = song.replace("\n", "")
            new_song_list.append(formatted_text_song)

    new_song_list_sorted = sorted(new_song_list)

    print(new_song_list_sorted)

    return new_song_list_sorted


def create_new_playlist_file(path, list_of_songs_file):
    sortedPlaylist = sortPlaylist(path, list_of_songs_file)

    with open("new_metal_playlist.txt", "w", encoding="utf-8") as file:
        for song in sortedPlaylist:
            file.write(song + "\n")

    print("Archivo creado correctamente.")


create_new_playlist_file(path, list_of_songs_file)
