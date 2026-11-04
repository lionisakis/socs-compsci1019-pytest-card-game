import pytest
import posixpath
from card_game.LoadCSV import *

def test_create_csv_reader_invalid_path(capsys):
    with pytest.raises(IOError):
        assert create_csv_reader("does_not_exist.csv"), "An error occurred" 
    out,err = capsys.readouterr()
    assert "An error occurred." in out 
    assert err is ''

CONTENT="""
Suit,Value
Hearts,10
Spades,Ace
Diamonds,7
"""
def test_create_csv_reader_valid_data(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert len(list(tmp_path.iterdir())) == 1
    # assert p == "1"
    # f = create_csv_reader()
    assert get_csv_rows(posixpath.abspath(p)) == CONTENT
