from plate import is_valid

def test_alphanumeric():
    assert is_valid("######") == False
    assert is_valid("AAAAAA") == True

def test_number_of_letter():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False
    assert is_valid("AAAAA") == True

def test_number_in_middle():
    assert is_valid("AA333A") == False

def test_two_letter():
    assert("A3333") == False
