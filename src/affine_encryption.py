

# AFFINE DECRYPTION:

# y ≡ ax + b (mod 26)
# ax ≡ y - b (mod 26)
# (a^-1)ax ≡ a^-1(y-b) (mod 26)
# x ≡ a^-1(y - b) (mod 26)

# a^-1 ≡ a^(φ(m)-1) (mod 26)
# a^-1 ≡ a^11 (mod 26)
# r ≡ a^11 (mod 26) => r = (a**11) % 26

# => x ≡ r(y - b) (mod 26)

def affine_encryption_wfct(a, b, message):
    message = list(message)
    number_msg_enc = [ord(char) - ord('a') for char in message]
    number_msg_dec = []
    p = a**11
    r = p % 26
    for y in number_msg_enc:
        x = y - b
        x *= r
        x %= 26
        number_msg_dec.append(x)
        
    dec_message = ''.join(chr(num + ord('a')) for num in number_msg_dec)
    return dec_message.upper()
        



def affine_encryption(message):
    print()
    print('Begin the analyse for affine encryption without knowing the function...')
    print()
    
    # transform the str message in a list with its characters : 'test' -> ['t', 'e', 's', 't']
    enc_message = list(message)
    # list of equivalent number in the alphabet (a->0, b->1, ..., z->25)
    number_msg_enc = [ord(char) - ord('a') for char in enc_message]
    
    # variables
    number_msg_dec_i = []   # i th decrypted possibilities on the form of a list of numbers
    possibilities = []  # list of the decrypted possibilities
    a_list = []
    b_list = []
    
    for a in range(25):
        a += 1
        for b in range(25):
            b += 1
            number_msg_dec_i = []
            dec_message_i = ''
            for i in range(len(number_msg_enc)):
                y = number_msg_enc[i]
                p = a**11
                r = p % 26
                x = y - b
                x *= r
                x %= 26
                number_msg_dec_i.append(x)
            dec_message_i = ''.join(chr(num + ord('a')) for num in number_msg_dec_i)
            possibilities.append(dec_message_i.lower())
            a_list.append(a)
            b_list.append(b)
            
            point = '.'
            nb_point = (b%3)+1
            print(f'Analyse{point*nb_point}')
            
    return possibilities, a_list, b_list
            
            

            
    
    

def display_single_pos_ae(dec_message):
    print()
    print('Analyse.')
    print('Analyse..')
    print('Analyse...')
    print()
    print(f'Decrypted message:  {dec_message}')
    print()

def display_pos_ae(a, b, decrypted_pos):
    print()
    print('RESULTS: ')
    for i in range(len(decrypted_pos)):
        print(f'{i}.  possibility:    {decrypted_pos[i].upper()}, a: {a[i]}, b:   {b[i]}\n')
    print()