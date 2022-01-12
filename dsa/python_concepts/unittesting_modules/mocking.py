from unittest.mock import Mock
#import json


mock = Mock()
json = mock

json.loads('{"key": "value"}')

## some assertions which self explainatory
print(json.loads.assert_called())
print(json.loads.assert_called_once())
print(json.loads.assert_called_with('{"key": "value"}'))
#print(json.loads.assert_called_with('{"key": "value1"}')) ## raises an error as args differ 


json.loads('{"key": "value"}')
#print(json.loads.assert_called_once()) ## raises an error as its called multiple times



## some attributes of the mock method

# Number of times you called loads():
print(json.loads.call_count)

# The last loads() call:
print(json.loads.call_args)


# List of loads() calls:
print(json.loads.call_args_list)

# List of calls to json's methods (recursively):
print(json.method_calls)
