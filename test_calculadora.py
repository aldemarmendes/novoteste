import pytest

from result import soma, sub, mult, div

def test_calculadora:
    
    assert soma(6,7) == 13
    assert sub (6,6) == 0
    assert mult(7,2) == 14
    assert div (4,2) == 2
    
    
    
    


