print("Welcome Caesar Cipher Program")

def encode():
    encode_input = input("Type your Message\n").lower()
    encoded_result = ""
    shift_input = int(input("Type your shift number\n"))
    for char in encode_input:
        if char.isalpha():
            exceeded = ord(char) + shift_input
            if exceeded > 122: 
                temp = 96 + (exceeded - 122)
                encoded_result += chr(temp)
            else:
                encoded_result += chr(exceeded)
        else:
            encoded_result += char
               
    print(f"Encoded res : {encoded_result}")

def decode():
    decode_input = input("Type your message\n").lower()
    decoded_result = ""
    shift_input = int(input("Type your shift number\n"))
    for char in decode_input:
        if char.isalpha():
            count = ord(char) - shift_input
            if count < 97:
                temp = 123 - (97 - count)
                decoded_result += chr(temp)
            else:
                decoded_result += chr(count)
        else:
            decoded_result += char
    
    print(f"Decoded res : {decoded_result}")

bool = True

while(bool):
    encrypt_input = input("'encode' or 'decode'\n").lower()

    if encrypt_input == 'encode':
        encode()
    else:
        decode()
    
    code_loop = input("Do you run this program again? 'y' or 'n' : ").lower()
    if(code_loop == 'n'):
        bool = False
    else:
        None