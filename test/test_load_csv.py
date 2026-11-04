import pytest

from card_game.LoadCSV import *

def test_create_csv_reader_invalid_path(capsys):
    with pytest.raises(IOError):
        assert create_csv_reader("does_not_exist.csv"), "An error occurred" 
    out,err = capsys.readouterr()
    assert "An error occurred." in out 
    assert err is ''
