from lib.count_words import *

def test_count_words_if_zero():
    assert count_words("")==0
def test_count_words_if_not_zero():
    assert count_words("this is not zero")==4