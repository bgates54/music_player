from player import Player


def main():
    songs = [
        "Jingle Bells",
         "Santa Claus is Coming to Town",
         "Winter Wonderland",
         "Christmas Carol",
         "All I Want for Christmas is You",
         "I'll Be Home for Christmas",
         "It's Beginning to Look a Lot Like Christmas",
         "Last Christmas",
         "Let It Snow",
         "White Christmas",
         "Rudolph the Red-Nosed Reindeer",
    ]
    music_player = Player(songs)
    music_player.run()

if __name__ == "__main__":
    main()

