from plates import is_valid

def test_nodigit():
    assert is_valid("HELLO")==True

def test_digitinmiddle():
    assert is_valid("CS52A5")==False

def test_digitatend():
    assert is_valid("SP7910")==True

def test_firstdigit0():
    assert is_valid("SP09")==False

def test_short():
    assert is_valid("S")==False

def test_long():
    assert is_valid("SHREY7910")==False

def test_spchar():
    assert is_valid("SHREY PATHAK'S BIKE.")==False

def test_wrongstart():
    assert is_valid("45SP")==False