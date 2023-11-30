from player import Player


def main():
    choice = int(input("[1] Christmas, [2] Alternative ---> "))
    if choice == 1:
        music_player = Player("Christmas")
    elif choice == 2:
        music_player = Player("Alternative")
    music_player.run()


if __name__ == "__main__":
    main()
