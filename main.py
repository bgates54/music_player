"""
FILE
    main.py
AUTHORS
    Brian Jernigan, Brynna Gates, Vincent Arcuri
DESCRIPTION
    Contains the main() function, which is the entry point for the music player.
"""
from player import Player


def main():
    """Instantiates the Player class, and runs the main loop."""
    music_player = Player()
    music_player.run()


if __name__ == "__main__":
    main()
