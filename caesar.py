import string

def caesar(message, key):
    letters_lowercase = string.ascii_lowercase
    letters_uppercase = string.ascii_uppercase
    alf_length = len(letters_lowercase)
    new_message = ""
    for index, letter in enumerate(message):


        if message[index].islower():
            if letters_lowercase.index(letter) + key > alf_length:
                new_position = key % alf_length
                new_letter = letters_lowercase[new_position]
                new_message = new_message + letters_lowercase[new_position]

            else:
                new_position = letters_lowercase.index(letter) + key
                new_message = new_message + letters_lowercase[new_position]

        elif message[index].isupper():
            if letters_uppercase.index(letter) + key > alf_length:
                new_position = key % alf_length
                new_letter = letters_uppercase[new_position]
                new_message = new_message + letters_uppercase[new_position]
            else:
                new_position = letters_uppercase.index(letter) + key
                new_message = new_message + letters_uppercase[new_position]

    return new_message

message = input("Enter message to encrypt: ")
encryption_key = int(input("Enter ecryption key: "))
print(caesar(message, encryption_key))


