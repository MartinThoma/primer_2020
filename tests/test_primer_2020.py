"""Unit Tests for the __init__.py of the primer_2020 package."""

# Third party modules
import pytest

# Internal modules
import primer_2020


def test_factorize_errors():
    """Test if wrong input throws a value error."""
    with pytest.raises(ValueError):
        primer_2020.factorize("14")

    with pytest.raises(ValueError):
        primer_2020.factorize(14.0)


def test_factorize_special_cases():
    """Test the behavior for valid, but special input"""
    assert primer_2020.factorize(1) == [1]
    assert primer_2020.factorize(-1) == [-1]
