# Day 39: Dunder Methods

class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.tracks = []

    def add(self, track: str):
        self.tracks.append(track)

    def __len__(self):
        return len(self.tracks)

    def __str__(self):
        return f"Playlist '{self.name}' with {len(self)} tracks"

    def __repr__(self):
        return f"Playlist(name={self.name!r}, tracks={self.tracks!r})"

pl = Playlist("Focus Beats")
pl.add("Lo-Fi Study")
pl.add("Deep Flow")
print(str(pl))
print(repr(pl))
print(f"Track count: {len(pl)}")
