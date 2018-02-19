def menu():
    UI = int(input("""
_____________________________________________________________________________

MAIN MENU
1. ENCODE
2. DECODE
3. CRACK
4. EXIT

_____________________________________________________________________________
"""))
    if UI == 1:
        plaintext = str(input("Enter the text to encode: "))
        Rotation = int(input("Enter the number of rotations: "))
        encryption(Rotation, plaintext)
        results(plaintext, Rotation)
    if UI == 2:
        plaintext = str(input("Enter a text to decode: "))
        Rotation = int(input("Enter the number of rotations: "))
        Rotation = Rotation - Rotation * 2
        encryption(Rotation, plaintext)
        results(plaintext, Rotation)
    if UI == 3: 
        crack()
        
    if UI == 4:
        confirmation = input("""Are you sure?
Y/N? """)
        if confirmation == 'Y' or confirmation == 'y':
            quit()


def crack():
    plaintext = str(input("Enter the text to Crack: "))
    crack = []
    maxlim = int(input("Enter the maximum number of cracks: "))
    maxlim = maxlim + 1
    for i in range(1,):
        res = ''
        for x in plaintext.lower():
            Wow = (Key.index(x)+ i) % 27
            res += Key[Wow]
        crack.append(res)
    print (crack)

def encryption(Rotation, plaintext):
    res = ''
    for x in plaintext.lower():
        try:
            i = (Key.index(x)+ Rotation) % 27
            res += Key[i]
        except ValueError:
            res += x
    return res.lower()
    


def results(plaintext, Rotation):
    encrypted = encryption(Rotation, plaintext)
    print ('Rotation: %s' % Rotation)
    print ('Encrypted: %s' % encrypted)
    print ('Text: %s' % plaintext)




print("""/\  ___\   /\  __ \   /\  ___\   /\  ___\   /\  __ \   /\  == \      /\  ___\   /\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \   
\ \ \____  \ \  __ \  \ \  __\   \ \___  \  \ \  __ \  \ \  __<      \ \ \____  \ \ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<   
 \ \_____\  \ \_\ \_\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\ \_\     \ \_____\  \ \_\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/      \/_____/ """)

x = 1

Key = " abcdefghijklmnopqrstuvwxyz"

count = 0
while count == 0:
    menu()
