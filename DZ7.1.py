# первая функция с проверкой assert - если всто ок - то True и принтуется ок

def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
print("ok")
assert say_hi("Yevhen", 43) == "Hi. My name is Yevhen and I'm 43 years old"
print("OK")
