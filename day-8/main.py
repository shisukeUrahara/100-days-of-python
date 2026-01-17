alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_or_decrypt(original_text, shift_amount, is_encrypt):
    list_text = list(original_text)

    if not is_encrypt:
        shift_amount *= -1

    for i, letter in enumerate(list_text):
        lower = letter.lower()

        if lower in alphabet:
            alpha_index = alphabet.index(lower)
            new_letter = alphabet[(alpha_index + shift_amount) % 26]

            # keep original case if you want
            list_text[i] = new_letter.upper() if letter.isupper() else new_letter
        # else: keep as-is (spaces, punctuation)

    print(''.join(list_text))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if(direction.lower() == 'encode'):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt_or_decrypt(text,shift,True)
elif(direction.lower() == 'decode'):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt_or_decrypt(text,shift,False)
else:
    text = input("Choose correct option please:\n").lower()


