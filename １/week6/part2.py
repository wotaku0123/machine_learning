x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay. ")
    print(' I sleep all night and I work all day. ')

print('Yo')
x = x + 2
print(x)
print_lyrics()

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')

def greet():
    return "Hello"

# print(greet(), "Glenn")
# print(greet('en'), 'Glenn')

def addtwo(a, b):
    added = a + b
    return added

print(addtwo(10, 30))