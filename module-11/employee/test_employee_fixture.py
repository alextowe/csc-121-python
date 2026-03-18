import pytest  # type: ignore
from employee import Employee

@pytest.fixture
def employee():
    return Employee('Alex', 'Towe', 50000)

def test_give_default_raise(employee):
    """Test that the default raise is added to the salary."""
    employee.give_raise()
    assert employee.salary == 55000

def test_give_custom_raise(employee):
    """Test that a custom raise is added to the salary."""
    employee.give_raise(10000)
    assert employee.salary == 60000