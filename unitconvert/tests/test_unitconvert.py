
from unitconvert.distance import miles_to_km
def test_miles_to_km():
    # some known results
    assert miles_to_km(1) == 1.60934
    
from unitconvert.distance import km_to_miles    
def test_km_to_miles():
    # some known results
    assert km_to_miles(1.60934) == 1
    
from unitconvert.temperature import fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    # some known results
    assert fahrenheit_to_celsius(32) == 0

from unitconvert.temperature import celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    # some known results
    assert celsius_to_fahrenheit(0) == 32


