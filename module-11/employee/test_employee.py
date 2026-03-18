from employee import Employee

def test_give_default_raise():
    """Test that the default raise is added to the salary."""
    emp = Employee('Alex', 'Towe', 50000)
    emp.give_raise()
    assert emp.salary == 55000

def test_give_custom_raise():
    """Test that a custom raise is added to the salary."""
    emp = Employee('Alex', 'Towe', 50000)
    emp.give_raise(10000)
    assert emp.salary == 60000