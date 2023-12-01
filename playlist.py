from song import Song


class Playlist:
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
        with open(filename, 'r') as fs:
            for line in fs:
                current_line = line.split(',')
                song = Song(current_line[0].strip(), current_line[1].strip(), current_line[2].strip())
                self.songs.append(song)

    def show_queue(self):
        for i in self.songs:
            print(i)



