calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    count_calls()
    return length, upper, lower

def is_contains(string, list_to_search):
    count_calls()
    len(string)
    for i in list_to_search:
        if i == string:
            return True
        else:
            return False

print(string_info("Betterye"))
print(string_info("Beterry"))
print(is_contains("Bettery", ("BeTery", "Bettery")))
print(calls)