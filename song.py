"""
FILE
    song.py
AUTHORS
    Brian Jernigan, Brynna Gates, Vincent Arcuri
DESCRIPTION
    Object for holding song data.
"""
class Song:
    """
    Attributes
    ----------
    title: str
    artist: str
    duration: str
        Song duration in seconds.
    """
    def __init__(self, title: str, artist: str, duration: str):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return self.title + " by " + self.artist

    def __len__(self):
        return self.duration
