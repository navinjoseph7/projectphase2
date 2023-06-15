from lib.grammarstats import *

def test_grammarstats():
    grammar = GrammarStats()
    assert grammar.check("I am happy.")== True
    assert grammar.check("i am not happy")== False
    assert grammar.check("I am still not happy")== False
    assert grammar.check("still not happy.")== False
    assert grammar.percentage_good()==25