from listqueue import ListQueue
from liststack import ListStack
import sys
import random


class Player:

    def __init__(self, songs: list):
        self.song_list = songs
        self.song_queue = ListQueue(self.song_list)
        self.backlog = ListStack()
        
    
    def main_menu(self):
        """The main menu options of the music player."""

        print("\033c") # This clears the output from the terminal
        print("0: Play\n1: Quit\n")
        choice = input("--->")
        while choice not in ["0", "1"]:
            print("Not an option.")
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

        print("\033c") # This clears the output from the terminal
        if not self.song_queue.isEmpty():
            song = self.song_queue.pop()
            self.backlog.push(song)
            print(f"Now Playing:\t{song}")
            if not self.song_queue.isEmpty():
                print(f"Up Next:\t{self.song_queue.peek()}\n")
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
        """Shuffles the song queue."""
        # Shuffle all songs in the queue, except the current song.
        current_song = self.backlog.pop()
        # Convert the song_queue to a list, shuffle it, and convert it back to a queue.
        song_list = list(self.song_queue)
        random.shuffle(song_list)
        # Add the current song back to the front of the queue.
        song_list = [current_song] + song_list
        self.song_queue = ListQueue(song_list)
        print(self.song_queue)


    def reset(self):
        """Adds all the songs from song list back to the queue, and empties the backlog."""

        self.song_queue = ListQueue(self.song_list)
        self.backlog.clear()


    def play_options_choice_list(self):
        """Handles the options available if there is no last song to play."""

        if len(self.backlog) > 1:
            print("0: Main Menu, 1: Next, 2: Shuffle, 3: Last")
            return list("0123")
        else:
            print("0: Main Menu, 1: Next, 2: Shuffle")
            return list("012")
        






