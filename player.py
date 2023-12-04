"""
FILE
    player.py
AUTHORS
    Brian Jernigan, Brynna Gates, Vincent Arcuri
DESCRIPTION
    Module for the Player class that handles the UI for and functionality for the music player.
"""

import random
import datetime
from listqueue import ListQueue
from liststack import ListStack
from playlist import Playlist
import sys


class Player:
    """
    Holds the song playlists and provides play options for the user.

    Attributes
    ----------
    playlists: dict[str, Playlist]
        A dictionary with key, playlist name, and value a Playlist object.
    song_queue: ListQueue
        Contains the song queue for the selected playlist.
    backlog: ListStack
        Contains the songs that have been played.
    playlist_selection: str|None
        The selected playlist.

    Methods
    -------
    main_menu()
        The main menu options allow the user to select a playlist or quit.
    play_options()
        Present the available options for the playlist, such as next song.
    run()
        Starts the program loop.
    play()
        Plays the next song in the song queue, and displays the song/queue information.
    add_last()
        Adds the last song played back to the front of the song queue.
    shuffle()
        Shuffles the remaining songs in the song queue.
    reset()
        Adds all the songs from the selected playlist back to the song queue.
    play_options_choice_list()
        Defines the play options available based on the song queue.
    get_time_remaining(current_song_duration) -> str
        The amount of time remaining in the playlist including the current song.

    """

    def __init__(self):
        self.playlists = {
            "Christmas": Playlist("Christmas"),
            "Alternative": Playlist("Alternative")
        }
        self.song_queue = ListQueue()
        self.backlog = ListStack()
        self.playlist_selection = None

    def main_menu(self):
        """The main menu options of the music player."""
        print(f"{'*' * 50}")
        print("0: Play - Christmas\n1: Play - Alternative\n2: Quit\n")
        choice = input("--->")
        while choice not in list("012"):
            self.main_menu()
        match int(choice):
            case 0:
                self.playlist_selection = "Christmas"
                self.reset()
                self.play()
            case 1:
                self.playlist_selection = "Alternative"
                self.reset()
                self.play()
            case 2:
                sys.exit()

    def play_options(self):
        """Play options loops for skipping, playing last song, shuffling, or
        returning to the main menu."""
        choice_list = self.play_options_choice_list()
        choice = input("--->")
        while choice not in choice_list:
            print("Not an option.")
            self.play_options()
        match int(choice):
            case 0:
                self.reset()
                self.main_menu()
            case 1:
                self.play()
            case 2:
                self.shuffle()
                self.play()
            case 3:
                self.add_last()
                self.play()

    def run(self):
        """Program main loop."""
        while True:
            self.main_menu()

    def play(self):
        """Loads the next song and displays the song playing, the time remaining, and a list of songs up next.
        If there are no more songs it returns to main menu, and resets the song list."""
        if not self.song_queue.is_empty():
            song = self.song_queue.pop()
            self.backlog.push(song)
            print(f"{'*' * 50}")
            print(f"\nNow Playing\n-----------")
            print(f"{song}\n")
            print(f"Time Remaining\n----------")
            print(f"{self.get_time_remaining(song.duration)}\n")
            if len(self.song_queue) > 0:
                print(self.song_queue)
            self.play_options()
        else:
            self.reset()
            self.main_menu()

    def add_last(self):
        """Adds last song to the front of the queue."""
        # The last song in the back is the current song, so must pop twice.
        current_song = self.backlog.pop()
        last_song = self.backlog.pop()
        self.song_queue = ListQueue([last_song, current_song]) + self.song_queue

    def shuffle(self):
        """Shuffles the songs left in the song queue."""
        current_song = self.backlog.pop()
        queue = list(self.song_queue)
        random.shuffle(queue)
        song_list = [current_song] + queue
        self.song_queue = ListQueue(song_list)

    def reset(self):
        """Adds all the songs from selected playlist back to the queue, and empties the backlog."""
        self.song_queue = ListQueue(self.playlists[self.playlist_selection])
        self.backlog.clear()

    def play_options_choice_list(self) -> list:
        """Handles the options available if there is no last song to play."""

        print("Options")
        print("--------")
        if len(self.backlog) > 1:
            print("0: Main Menu, 1: Next, 2: Shuffle, 3: Last")
            return list("0123")
        else:
            print("0: Main Menu, 1: Next, 2: Shuffle")
            return list("012")

    def get_time_remaining(self, current_song_duration) -> str:
        """Returns the time remaining of playlist in hh:mm:ss format"""
        duration = int(current_song_duration)
        for item in self.song_queue:
            duration += int(item.duration)
        return str(datetime.timedelta(seconds=duration))
