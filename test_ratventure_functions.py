import pytest
from RatVenture import *

def test_view_character():
    character = viewCharacter()
    assert character == viewCharacter()
