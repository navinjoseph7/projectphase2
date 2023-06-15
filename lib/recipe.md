# Describe the problem
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

# Design the Function Signature

def todo(text):

""" Checks if the input text has a string 'TODO' on it

Parameters : text : a string containing words (" todo : run 1 mile")

returns : either true of false, if text contains todo then true else false

side effects: no side effects but better to change everything into one case at the beginning to avoid confusions. """


# Create Examples as Tests
"""
 Given a text with todo 
 It returns true 
"""
todo("TODO : run a mile")=> True

"""
 Given a text without todo
 It returns false 
"""
todo("nothing to do ")=> false

"""
 Give an empty string
 It returns false
"""
todo("")=> false



