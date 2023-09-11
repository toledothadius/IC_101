text = input("Text: ")

x = len(text)

UPPERCASE = 0
LOWERCASE = 0

for character in text:
    if(character.isupper()):
        UPPERCASE += 1
    if(character.islower()):
        LOWERCASE += 1

print("Lowercase:",LOWERCASE)
print("Uppercase:",UPPERCASE)
print("The Count Of Letters: ", x)