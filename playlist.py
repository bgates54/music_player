"""
FILE
    playlist.py
AUTHORS
    Brian Jernigan, Brynna Gates, Vincent Arcuri
DESCRIPTION
    Builds a playlist from a text file.
"""
from song import Song


class Playlist:
    """
    A list of songs.

    Attributes
    ----------
    name: str
        Playlist name matching to a text file.
    songs: list[Song]
        A list of Song objects.

    Methods
    -------
    load_songs()
        Creates the song list from a text file.
    """

    def __init__(self, name):
        self.name = name
        self.songs = []
        self.load_songs(name + ".txt")

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return self.name

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self.songs[cursor]
            cursor += 1

    def load_songs(self, filename: str):
        """Reads the song data from a text file, creates Song objects from the data,
        and adds them to the list of songs."""
        with open(filename, 'r') as fs:
            for line in fs:
                current_line = line.split(',')
                song = Song(current_line[0].strip(), current_line[1].strip(), current_line[2].strip())
                self.songs.append(song)
