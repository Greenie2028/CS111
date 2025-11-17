# Remember to import from the lab06 file and pytest
import pytest
from lab06 import *
# Write your test code here for Q1

def test_product():
    assert product(3) == 6, "Incorrect output"
    assert product(12) == 479001600, "Incorrect output"
    assert product(1) == 1, "Incorrect output"
    with pytest.raises(ValueError):
        product(0)
    with pytest.raises(ValueError):
        product("Hello")
    with pytest.raises(ValueError):
        product(-1)
    
def test_summation():
    assert summation(5) == 15, "Incorrect output"
    assert summation(0) == 0, "Incorrect output"
    assert summation(1) == 1, "Incorrect output"
    assert summation(15) == 120, "Incorrect output"
    with pytest.raises(ValueError):
        product("Hello")
    with pytest.raises(ValueError):
        product(-1)


# Q2
#####################################

def test_square():
    assert square(3) == 9, "Incorrect output"
    assert square(1) == 1, "Incorrect output"
    assert square(13) == 169, "Incorrect output"
    assert square(-1) == 1, "Incorrect output"
    
def test_sqrt():
    """*** YOUR CODE HERE ***"""
    assert sqrt(16) == 4, "Incorrect output"
    assert sqrt(4) == 2, "Incorrect output"
    assert sqrt(3) == 3**0.5, "Incorrect output"

def test_mean():
    """*** YOUR CODE HERE ***"""
    assert mean([1,2,3]) == 2, "Incorrect output"
    assert mean([3,3,3]) == 3, "Incorrect output"
    assert mean([10]) == 10, "Incorrect output"
    assert mean([0]) == 0, "Incorrect output"
    assert mean([-1]) == -1, "Incorrect output"
    with pytest.raises(AssertionError):
        std_dev("Hello")
    with pytest.raises(AssertionError):
        std_dev([]) 
    with pytest.raises(AssertionError):
        std_dev(10)

def test_median():
    """*** YOUR CODE HERE ***"""
    assert median([4,7,3,10,6]) == 6, "Incorrect output"
    assert median([1,3,2]) == 2, "Incorrect output"
    assert median([10]) == 10, "Incorrect output"
    assert median([-3,0,1,-1,0]) == 0, "Incorrect output"
    assert median([0,1,6,4,2,4,3]) == 3, "Incorrect output"
    assert median([3,5,7,9]) == 6, "Incorrect output"
    with pytest.raises(AssertionError):
        std_dev("Hello")
    with pytest.raises(AssertionError):
        std_dev([]) 
    with pytest.raises(AssertionError):
        std_dev(10)

def test_mode():
    """*** YOUR CODE HERE ***"""
    assert mode([1,2,2]) == 2, "Incorrect output"
    assert mode([1,1,2,2,3]) == 1, "Incorrect output"
    assert mode([1,1,2,1,3]) == 1, "Incorrect output"
    with pytest.raises(AssertionError):
        std_dev("Hello")
    with pytest.raises(AssertionError):
        std_dev([]) 
    with pytest.raises(AssertionError):
        std_dev(10)

def test_std_dev():
    """*** YOUR CODE HERE ***"""
    with pytest.raises(AssertionError):
        std_dev("Hello")
    with pytest.raises(AssertionError):
        std_dev([]) 
    with pytest.raises(AssertionError):
        std_dev(10) 
    assert std_dev([10,12,13,6,12]) == pytest.approx(2.569, 0.1), "Incorrect output"
    assert std_dev([1,1,1,1,1]) == 0, "Incorrect output"
    assert std_dev([0,0,0,0,1]) == pytest.approx(0.4, 0.1), "Incorrect output"
    assert std_dev([10000,1,1,1,1]) == pytest.approx(3996.6, 0.1), "Incorrect output"
def test_stat_analysis():
    """*** YOUR CODE HERE ***"""
    assert mean([1,2,3]) == 2, "Incorrect output"
    assert mean([3,3,3]) == 3, "Incorrect output"
    assert mean([10]) == 10, "Incorrect output"
    assert mean([0]) == 0, "Incorrect output"
    assert mean([-1]) == -1, "Incorrect output"
    assert median([4,7,3,10,6]) == 6, "Incorrect output"
    assert median([1,3,2]) == 2, "Incorrect output"
    assert median([10]) == 10, "Incorrect output"
    assert median([-3,0,1,-1,0]) == 0, "Incorrect output"
    assert median([0,1,6,4,2,4,3]) == 3, "Incorrect output"
    assert median([3,5,7,9]) == 6, "Incorrect output"
    assert mode([1,2,2]) == 2, "Incorrect output"
    assert mode([1,1,2,2,3]) == 1, "Incorrect output"
    assert mode([1,1,2,1,3]) == 1, "Incorrect output"
    with pytest.raises(AssertionError):
        std_dev("Hello")
    with pytest.raises(AssertionError):
        std_dev([]) 
    with pytest.raises(AssertionError):
        std_dev(10) 
    assert std_dev([10,12,13,6,12]) == pytest.approx(2.569, 0.1), "Incorrect output"
    assert std_dev([1,1,1,1,1]) == 0, "Incorrect output"
    assert std_dev([0,0,0,0,1]) == pytest.approx(0.4, 0.1), "Incorrect output"
    assert std_dev([10000,1,1,1,1]) == pytest.approx(3996.6, 0.1), "Incorrect output"
    with pytest.raises(AssertionError):
        std_dev("Hello")
    with pytest.raises(AssertionError):
        std_dev([]) 
    with pytest.raises(AssertionError):
        std_dev(10)
# OPTIONAL
#####################################

def test_accumulate():
    """*** YOUR CODE HERE ***"""


def test_product_short():
    """*** YOUR CODE HERE ***"""


def test_summation_short():
    """*** YOUR CODE HERE ***"""


def test_invert():
    """*** YOUR CODE HERE ***"""


def test_change():
    """*** YOUR CODE HERE ***"""


def test_invert_short():
    """*** YOUR CODE HERE ***"""


def test_change_short():
    """*** YOUR CODE HERE ***"""
