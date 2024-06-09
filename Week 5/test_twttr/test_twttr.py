from twttr import shorten

def test_shorten():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
