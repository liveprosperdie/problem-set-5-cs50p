from twttr import shorten

def test_lower():
    assert shorten("helloworld")=="hllwrld"
    assert shorten("hello world@324")=="hll wrld@324"


def test_uppercase():
    assert shorten("HELLOWORLD")=="HLLWRLD"
    assert shorten("HELLO WORLD@324")=="HLL WRLD@324"


def test_novowel():
    assert shorten("shh dnt tlk")=="shh dnt tlk"


def test_mix():
    assert shorten("HEllo World@")=="Hll Wrld@"


def test_empty():
    assert shorten("")==""