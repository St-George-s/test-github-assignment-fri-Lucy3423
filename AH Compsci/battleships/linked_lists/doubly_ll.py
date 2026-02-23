class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_song(self, title):
        new_song = SongNode(title)
        if self.head is None:
            self.head = new_song
            self.prev = new_song
        else:
            self.tail = new_song
            new_song.prev = self.tail
            self.tail = new_song
        
    def play_forward(self):
        current = self.head
        while current is not None:
            print(f"Now playing: {current.title}")
            current = current.next
    
    def play_backward(self):
        current = self.tail
        while current.prev is not None:
            print(f"Now playing {current.title}")
            current = current.prev

    def find_song_forward(self, title):
        current = self.head
        while current:
            if current.title == title:
                return True
            current = current.next
        return False
    
# main
playlist = Playlist()
playlist.add_song("Shake it off")
playlist.add_song("Flume")
playlist.add_song("Blue")
# found = playlist.find_song_forward("Flume")
# print(found)
playlist.play_backward()