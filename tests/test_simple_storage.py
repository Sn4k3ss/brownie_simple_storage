from brownie import SimpleStorage, accounts


# Testing is essential to become a successfull blockchain engineer
# 
# use 'brownie test --pdb' to open a python environment (like a debugger) to see what is happening in the code 
#
#
#

def test_deploy():
    
    # Arrange
    account = accounts[0]
    
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    
    # Assert
    assert starting_value == expected


def test_updating_value():

    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    
    # Act
    expected = 15
    starting_value = simple_storage.store(expected, {"from": account})
    
    # Assert
    assert expected == simple_storage.retrieve()