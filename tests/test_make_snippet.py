from lib.make_snippet import *

def test_make_snippet():
    assert make_snippet("")==""

def test_make_snippet_less_than_five():
    assert make_snippet("This is nothing")== "This is nothing"

def test_make_snippet_more_than_five():
    assert make_snippet ("This is more than five words")== "This is more than five ..."