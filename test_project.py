from project import validate_input, process_action
from FunctionsAndClasses.show_menu import is_valid_email

def main():
    test_is_valid_email()
    test_validate_input()
    test_process_action()
    
def test_is_valid_email():
    assert is_valid_email("marko@gmail.com") == True
    assert is_valid_email("marko@@gmail.com") == False
    assert is_valid_email("marko@gmail..com") == True
    
    
def test_validate_input():
    status, choice = validate_input(2, 1, 4)
    assert status == True
    status, choice = validate_input(0, 1, 4)
    assert status == False
    status, choice = validate_input(5, 1, 4)
    assert status == False
    status, choice = validate_input(4, 1, 4)
    assert status == False
    
    
def test_process_action():
    assert process_action(0, 1) == False
    assert process_action(1, 5) == False