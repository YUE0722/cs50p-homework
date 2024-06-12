from numb3rs import validate

def test_validate():
    assert validate("0.0.0.0") == False
    assert validate("256.256.256.256") == False
    assert validate("hello") == False
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
