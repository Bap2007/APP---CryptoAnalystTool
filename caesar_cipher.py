

def caesar_cipher_wgap(gap, enc_message):
    enc_message = list(enc_message)
    number_msg_enc = [ord(char) - ord('a') for char in enc_message]
    number_msg_dec = []
    for e in number_msg_enc:
        f = (e - gap) % 26
        number_msg_dec.append(f)
    dec_message = ''.join(chr(num+ord('a')) for num in number_msg_dec)
    return dec_message.upper()
        

def caesar_cipher(message):
    pass