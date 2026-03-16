from bank import value

def test_lowerhello():
    assert value("hello shrey")==0

def test_lowerh():
    assert value("hi shrey")==20

def test_lower():
    assert value("whats up shrey")==100

def test_upperhello():
    assert value("HELLO SHREY")==0

def test_upperh():
    assert value("HI SHREY")==20

def test_upper():
    assert value("WHATS UP SHREY")==100

def test_mixed():
    assert value ("HeLLO Shrey")==0
    assert value("HoWdie Shrey")==20
    assert value("WHats up SHrey")==100

def test_empty():
    assert value ("")==100