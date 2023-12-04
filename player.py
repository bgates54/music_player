import random
import datetime
from listqueue import ListQueue
from liststack import ListStack
from playlist import Playlist
import sys


class Player:
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
        print(f"{"*"*50}")
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
            print(f"{"*"*50}")
            print(f"\nNow Playing\n-----------")
            print(f"{song}\n")
            print(f"Time Remaining\n----------")
            print(f"{self.get_time_remaining(song.duration)}\n")
            if len(self.song_queue) > 0:
                print(self.song_queue)

            duration = 0
            for item in self.song_queue:
                duration += int(item.duration)
            in_minutes = int(duration / 60)
            in_seconds = duration % 60
            print(f"Time left in playlist: {in_minutes}:{in_seconds}\n")

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
        duration = int(current_song_duration)
        for item in self.song_queue:
            duration += int(item.duration)
        return str(datetime.timedelta(seconds=duration))

