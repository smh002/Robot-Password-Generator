"""Test for my functions."""

from my_module.functions import *

def test_password_generator_letters():
    """Tests password_generator_letters"""

    assert callable(password_generator_letters)
    assert isinstance(password_generator_letters(8), str)
    assert len(password_generator_letters(10)) == 10

def test_password_generator_letters_and_numbers():
    """Tests password_generator_letters_and_numbers"""

    assert callable(password_generator_letters_and_numbers)
    assert isinstance(password_generator_letters_and_numbers(5), str)
    assert len(password_generator_letters_and_numbers(7)) == 7
    
def test_password_generator_letters_and_punctuation():
    """Tests password_generator_letters_and_punctuation"""
    
    assert callable(password_generator_letters_and_punctuation)
    assert isinstance(password_generator_letters_and_punctuation(10), str)
    assert len(password_generator_letters_and_punctuation(5)) == 5

def test_password_generator_all():
    """Tests password_generator_all"""
    
    assert callable(password_generator_all)
    assert isinstance(password_generator_all(8), str)
    assert len(password_generator_all(3)) == 3

def test_generate_password():
    """Tests generate_password"""
    
    assert callable(generate_password)
    assert isinstance(generate_password(5, [5, True, True]), str)
    assert len(generate_password(8, [8, True, True])) == 8
    assert len(generate_password(10, [10, True, False])) == 10
    assert len(generate_password(15, [15, False, True])) == 15
    assert len(generate_password(5, [5, False, False])) == 5

def test_all():
    """tests all test functions"""
    
    test_password_generator_letters()
    test_password_generator_letters_and_numbers()
    test_password_generator_letters_and_punctuation()
    test_password_generator_all()
    test_generate_password()