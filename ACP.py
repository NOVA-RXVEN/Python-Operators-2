print("\033c")
char = input("Enter A Character: ")

if char >="a" and char <= "z":
    print(f"The Character {char} is a LowerCase Alphabet")
    
elif char >= "A" and char <= "Z":
    print(f"The Character {char} is an UpperCase Alphabet")
    
else:
    print(f"The Charater {char} is NOT an Alphabet you Idiot!")         