

def caesar_cipher_wgap(gap, enc_message):
    enc_message = list(enc_message)
    number_msg_enc = [ord(char) - ord('a') for char in enc_message]
    number_msg_dec = []
    for e in number_msg_enc:
        f = (e - gap) % 26
        number_msg_dec.append(f)
    dec_message = ''.join(chr(num + ord('a')) for num in number_msg_dec)
    return dec_message.upper()
        

def caesar_cipher(enc_message):
    print()
    print('Begin the analyse without knowing the gap...')
    print()
    # transform the str message in a list with its characters : 'test' -> ['t', 'e', 's', 't']
    enc_message = list(enc_message)
    # list of equivalent number in the alphabet (a->0, b->1, ..., z->25)
    number_msg_enc = [ord(char) - ord('a') for char in enc_message]
    
    # variables
    number_msg_dec_i = []   # i th decrypted possibilities on the form of a list of numbers
    possibilities = []  # list of the decrypted possibilities
    gaps = []           # gaps corresponding to each possibilities
    
    
    for i in range(25):
        number_msg_dec_i = []
        dec_message_i = ''
        gap = i + 1     # gap = 1, ..., 25
        for e in number_msg_enc:
            f = (e - gap) % 26
            number_msg_dec_i.append(f)
            
        dec_message_i = ''.join(chr(num + ord('a')) for num in number_msg_dec_i)
        
        dec_message_i = dec_message_i.upper()
        possibilities.append(dec_message_i)
        gaps.append(gap)
        point = '.'
        nb_point = (i%3)+1
        print(f'Analyse{point*nb_point}')
        
    return possibilities, gaps