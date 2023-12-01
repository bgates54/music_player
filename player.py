import random

from listqueue import ListQueue
from liststack import ListStack
from playlist import Playlist
import sys


class Player:
    def __init__(self, playlist: str):
        self.playlist = Playlist(playlist)
        self.song_queue = ListQueue(self.playlist)
        self.backlog = ListStack()

    def main_menu(self):
        """The main menu options of the music player."""
        print("0: Play\n1: Quit\n")
        choice = input("--->")
        while choice not in ["0", "1"]:
            self.main_menu()
        match int(choice):
            case 0:
                self.play()
            case 1:
                sys.exit()

    def play_options(self):
        """Play options loops for skipping or playing last songs."""
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
        while True:
            self.main_menu()

    def play(self):
        """Displays the song playing, if no more songs it returns to main menu, and resets the song list."""
        if not self.song_queue.is_empty():
            song = self.song_queue.pop()
            self.backlog.push(song)
            print(f"Now Playing: {song}")
            print()
            if len(self.song_queue) > 0:
                print(self.song_queue)
            duration = 0
            for item in self.song_queue:
                duration += int(item.duration)
            print(f"Remaining Playlist Duration:\t{duration} seconds\n")
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
        current_song = self.backlog.pop()
        queue = list(self.song_queue)
        random.shuffle(queue)
        song_list = [current_song] + queue
        self.song_queue = ListQueue(song_list)


    def reset(self):
        """Adds all the songs from song list back to the queue, and empties the backlog."""
        self.song_queue = ListQueue(self.playlist)
        self.backlog.clear()

    def play_options_choice_list(self):
        """Handles the options available if there is no last song to play."""
        if len(self.backlog) > 1:
            print("0: Main Menu, 1: Next, 2: Shuffle, 3: Last")
            return list("0123")
        else:
            print("0: Main Menu, 1: Next, 2: Shuffle")
            return list("012")
