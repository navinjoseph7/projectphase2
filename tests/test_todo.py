from lib.todo import *

def test_todo():
    assert todo("TODO : run a mile") == True
def test_todo_without_todo():   
    assert todo("nothing to do ")== False
def test_todo_with_empty_string():
    assert todo("")== False