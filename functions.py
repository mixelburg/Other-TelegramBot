FILE_PATH = "Pink_Floyd_DB.txt"

ALBUM_DELIMITER = "#"
SONG_DELIMITER = "*"
INFO_DELIMITER = "::"


def extractor(file_path):
    """
    Extracts data from file in 'file_path' and
    separates it into dictionaries of dictionaries of dictionaries
    :param file_path: a file
    :return: data in a human readable format
    """
    with open(file_path, "r") as DB:
        lines = DB.read()
        lines = lines[1:]

        lines = lines.split(ALBUM_DELIMITER)

        albums = []
        for album in lines:
            albums.append(album.split(SONG_DELIMITER))

        # get albums
        data = {}
        for album in albums:
            album_info = {}
            album_data = album[0].split(INFO_DELIMITER)
            album_info["date"] = album_data[1]

            # get data for each song
            songs = {}
            for x in range(1, len(album)):
                song = {}
                song_data = album[x].split(INFO_DELIMITER)
                song["singer"] = song_data[1]
                song["length"] = song_data[2]
                song["lyrics"] = song_data[3]
                songs[song_data[0]] = song

            album_info["songs"] = songs

            data[album_data[0]] = album_info

        return data


DATA = extractor(FILE_PATH)


def get_album_list():
    """
    takes all keys of 'data' dictionary
    and returns them (returns names of albums)
    :param data: source
    :return: string that represents album list
    """
    data = DATA

    albums_list = "Album list: \n"
    for album_name in data:
        albums_list += album_name
        albums_list += ", "

    return albums_list


def get_song_list(album_name):
    """
    gives you a list of songs in a given album
    :param data: source
    :param album_name:
    :return: string: names of songs
    """
    data = DATA

    if album_name in data:
        song_list = "Songs: \n"
        for song in data[album_name]["songs"]:
            song_list += song
            song_list += "\n"
        return song_list
    else:
        return "[!] album does not exist\n "


def get_song_length(song_name):
    """
    gives you a length of a song by a given name
    :param data: source
    :param song_name:
    :return: string: length of a song
    """
    data = DATA

    for album in data:
        for song in data[album]["songs"]:
            if song == song_name:
                return data[album]["songs"][song]["length"]
    return "[!] Song not found\n"


def get_song_lyrics(song_name):
    """
    gives you lyrics of a song by a given name
    :param data: source
    :param song_name:
    :return: string: lyrics of a song
    """
    data = DATA

    for album in data:
        for song in data[album]["songs"]:
            if song == song_name:
                return data[album]["songs"][song]["lyrics"]
    return "[!] Song not found\n"


def get_source_album(song_name):
    """
    gives you a name of album containing given song
    :param data: source
    :param song_name:
    :return: string: name of an album
    """
    data = DATA

    for album in data:
        for song in data[album]["songs"]:
            if song == song_name:
                return album
    return "[!] Song not found\n"


def find_song_name(song_name):
    """
    gives you names of songs containing given substring
    :param data: source
    :param song_name:
    :return: string: song names
    """
    data = DATA

    names = ""
    for album in data:
        for song in data[album]["songs"]:
            if song_name.lower() in song.lower():
                names += ("'" + song + "'" + " from album: " + album + ", ")
    if names == "":
        return "[!] Nothing found\n"
    return names


def find_song_lyrics(text):
    """
    gives you songs which lyrics contain given substring
    :param data: source
    :param text: substring
    :return: string: song names
    """
    data = DATA

    names = ""
    for album in data:
        for song in data[album]["songs"]:
            if text.lower() in data[album]["songs"][song]["lyrics"].lower():
                names += ("'" + song + "'" + " from album: " + album + ", ")
    if names == "":
        return "[!] Nothing found\n"
    return names

