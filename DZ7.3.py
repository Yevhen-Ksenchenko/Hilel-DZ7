def second_index(text, some_str):
    index1 = text.find(some_str)
    if index1 == -1:
        return None
    index2 = text.find(some_str, index1 + 1)
    if index2 != -1:
        return index2
    else:
        return None

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", "h") is None
assert second_index("Hello, hello", "lo") == 10
print('ОК')