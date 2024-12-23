calls = 0

def count_calls():
    global calls
    calls +=1

def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return length, upper, lower

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_to_search = [x.lower() for x in list_to_search]
    if string_lower in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)