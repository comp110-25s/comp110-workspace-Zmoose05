__author__: str = "73055996"

import pytest
from dictionary import invert
from dictionary import favorite_color
from dictionary import count
from dictionary import bin_len


def test_invert1() -> None:
    """Use case 1 for invert"""
    assert invert({"A": "B", "C": "D"}) == {"B": "A", "D": "C"}


def test_invert2() -> None:
    """Use case 2 for invert"""
    assert invert({"girl": "boy", "cat": "dog"}) == {"boy": "girl", "dog": "cat"}


def test_invert3() -> None:
    """Edge case for invert"""
    assert invert({}) == {}


with pytest.raises(KeyError):
    """Key error test for invert"""
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)


def test_count1() -> None:
    """Use case 1 for count"""
    assert count(["red", "red", "blue"]) == {"red": 2, "blue": 1}


def test_count2() -> None:
    """Use case 2 for count"""
    assert count(["boy", "girl", "boy", "girl", "girl"]) == {"boy": 2, "girl": 3}


def test_count3() -> None:
    """Edge case for count"""
    assert count([]) == {}


def test_favorite_color1() -> None:
    """Use case 1 for favorite_color"""
    assert favorite_color({"bob": "red", "jim": "green", "bill": "green"}) == "green"


def test_favorite_color2() -> None:
    """Use case 2 for favorite_color"""
    assert (
        favorite_color(
            {
                "joe": "purple",
                "greg": "green",
                "jill": "green",
                "amy": "purple",
                "ruth": "purple",
            }
        )
        == "purple"
    )


def test_favorite_color3() -> None:
    """Edge case for favorite_color"""
    assert favorite_color({}) == ""


def test_bin_len1() -> None:
    """Use case 1 for bin_len"""
    assert bin_len(["blue", "cow", "farm", "toy", "toys"]) == {
        3: {"cow", "toy"},
        4: {"blue", "farm", "toys"},
    }


def test_bin_len2() -> None:
    """Use case 2 for bin_len"""
    assert bin_len(["cram", "beware", "sleepy", "excited", "hi", "flabbergasted"]) == {
        2: {"hi"},
        4: {"cram"},
        6: {"beware", "sleepy"},
        7: {"excited"},
        13: {"flabbergasted"},
    }


def test_bin_len3() -> None:
    """Edge case for bin_len"""
    assert bin_len([]) == {}
