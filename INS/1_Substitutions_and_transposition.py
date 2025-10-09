#A python program to illustrate Caesar Cipher Technique 
def encrypt(text,s):
    result = ""
    # traverse text 
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters 
        if(char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
# Encrypt lowercase characters 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
#check the above function
text=input(" Enter the text to encrypt ")
s = 3 
print("Text :- " + text) 
print(f"Shift :- {str(s)}")
print( "Cipher :- " + encrypt(text,s)) 

# Code to implement railfence

print("\n")
def RailFence(txt):
    result="" 
    for i in range(len(txt)):
        if(i%2==0):
            result+=txt[i]
    for i in range(len(txt)):
        if(i%2!=0):
            result += txt[i]
    return result

org =input("enter a txt\n")
print(f"Ciphered Text :- {RailFence(org)}")