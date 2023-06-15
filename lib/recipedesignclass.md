# Describe the problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

# Design the Class Interface
 
# EXAMPLE

class TrackMusic:
    # User-facing properties:
    #   musiclist: list

    def __init__(self):
        # Parameters:
        #   musiclist: list
        # Side effects:
        #   initializes the musiclist to an empty list
        pass # No code here yet

    def add_music(self, track):
        # Parameters:
        #   track: string representing a music track
        # Returns:
        #   Nothing
        # Side-effects
        #   adds the music track  to the self object if it's not already in the list.
        pass # No code here yet

    def display_list(self):
        # Returns:
        #   A list containing all the music tracks he has listened
        # Side-effects:
        #   Throws an exception if no music has been listened
         # No code here yet

# EXAMPLE

"""
Given a new track to add
#add adds the track to the list and display_list displays the name of the track
"""
trackmusic = TrackMusic()
trackmusic.add("Waka Waka")
trackmusic.display_list() # => ["Waka Waka"]

"""
Asks to display the list without adding any to it
#display_list raises an exception
"""
trackmusic = TrackMusic()
trackmusic.display_list() # raises an error with the message "No tracks listened ."

"""
Given multiple tracks to add
#add add the tracks to the list and display_list displays it as a single list
"""
trackmusic = TrackMusic()
trackmusic.add("Waka Waka")
trackmusic.add("Me and my broken heart")
trackmusic.add("Love me like you do")
trackmusic.display_list() # => ["Waka Waka","Me and my broken heart","Love me like you do"]