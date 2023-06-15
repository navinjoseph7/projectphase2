class TrackMusic:
    def __init__(self):
        self.musiclist = []
    def add_music(self, track):
        if track not in self.musiclist:
            self.musiclist.append(track)
    def display_list(self):
        if self.musiclist == []:
            raise Exception("No tracks listened")
        else:
            return self.musiclist
        
