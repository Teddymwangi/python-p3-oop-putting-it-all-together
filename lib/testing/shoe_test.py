import pytest
from lib.shoe import Shoe

def test_shoe_initialization():
    shoe = Shoe("Nike", "Black", 10)
    assert shoe.brand == "Nike"
    assert shoe.color == "Black"
    assert shoe.size == 10

def test_shoe_wear_and_take_off():
    shoe = Shoe("Nike", "Black", 10)
    shoe.wear()
    assert shoe.is_worn == True
    shoe.take_off()
    assert shoe.is_worn == False

if __name__ == "__main__":
    pytest.main()