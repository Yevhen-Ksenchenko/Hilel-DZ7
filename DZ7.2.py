def correct_sentence(text):
    if not text.endswith('.'):
        text += '.'
    text = str(text)
    return text[0].upper() + text[1:]

assert correct_sentence("greetings12, friends") == "Greetings12, friends."
print('ok')
assert correct_sentence("hello34") == "Hello34."
print('OK')
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
print('okey')
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
print('OKEY')
assert correct_sentence("greetings, friends.") == "Greetings, friends."
print('ОКey')
