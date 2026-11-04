import pytest

from card_game.LoadCSV import *

def test_create_csv_reader_invalid_path():
    assert create_csv_reader("sadsad") 

