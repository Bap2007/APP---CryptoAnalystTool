import pyfiglet # type: ignore
import os
from src.caesar_cipher import caesar_cipher, caesar_cipher_wgap, display_single_pos_cc, display_pos_cc
from src.affine_encryption import affine_encryption, affine_encryption_wfct, display_single_pos_ae, display_pos_ae


# GLOBAL VARIABLES
encrypted_msg = ''
algorithm = ''
algorithms = ['Caesar Cipher', 'Affine Encryption', 'Permutation', 'Vigenere Key']
decryption_pos = []

# 1. Caesar Cipher variables: y ≡ x + gap   (mod 26)
gap = None
cor_gaps = []
unknown_gap = True

# 2. Affine Encyption variables: y ≡ ax + b (mod 26)
a = None
b = None 

# 3. Permutation: y -> y'
s = [[], []]

# 4. Vigenere key: y = x + key[i]
key = ''






# BASIC FUNCTIONS
def rm_spaces(msg):
    msg = msg.replace(" ", "")
    msg = msg.lower()
    return msg


def save_to_file(data_list, name):
    os.makedirs('data', exist_ok=True)
    file_path = os.path.join('data', f'pos-{name}')
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:

            file.write(item + '\n')
            
    return file_path


def interactive_console():
    # TITLE + DESCRIPTION
    
    title  = pyfiglet.figlet_format('CryptoAnalyst')
    print(title)
    print()
    print('ENCRYPTION ALGORITHMS:')
    print('- Caesar Cipher      (1)')
    print('- Affine Encryption  (2)')
    print('- Permutation        (3)')
    print('- Vigenere Key       (4)')
    
    # MENU
    
    print()
    # type crpyted message
    try:
        encrypted_msg = input('Enter the message to decrypt:    ')
        encrypted_msg = str(encrypted_msg)
        encrypted_msg = rm_spaces(encrypted_msg)
    except:
        print("Do not enter special character, they are not supported yet!")
        
    print()
    
    # choose algorithm
    algorithm = input('Choose the algorithm you think was used to encrypt this message: ')
    while algorithm not in algorithms and algorithm not in ['1', '2', '3', '4']:
        print()
        print('Enter only one of the supported algorithm!')
        print()
        algorithm = input('Choose the algorithm you think was used to encrypt this message: ')
        
    print()
    
    
    # ALGORITHM CHOSEN  
    # 1. Caesar Cipher decryption
    if algorithm == 'Caesar Cipher' or algorithm == '1':
        print('CAESAR CIPHER:')
        print()
        print(f'Encrypted Message: {encrypted_msg.upper()}')
        # Ask if the gap is known
        is_gap_known = input('Do you know the gap used? [Y/n]   ')
        while not is_gap_known in ['Y', 'n']:
            print('Answer with Y (yes) or n (no) !')
            is_gap_known = input('Do you know the gap used? [Y/n]   ')

        # Gap known
        if is_gap_known == 'Y':
            try:
                gap = input('Enter the gap used: ')
                gap = int(gap)
            except:
                print('Answer with an integer number!')
                gap = input('Enter the gap used: ')
                
            decryption_pos = caesar_cipher_wgap(gap, encrypted_msg) 
            
            display_single_pos_cc(decryption_pos)

        # Gap Unknown
        else:
            res = caesar_cipher(encrypted_msg) 
            decryption_pos = res[0]
            cor_gaps = res[1]
            
            display_pos_cc(decryption_pos, cor_gaps)

    # 2. Affine Encryption
    if algorithm == 'Affine Encryption' or algorithm == '2':
        print('AFFINE ENCRYPTION:')
        print()
        print(f'Encrypted Message: {encrypted_msg.upper()}')
        is_fct_known = input('Do you know the function used (y ≡ ax + b (mod 26) )? [Y/n]:  ')
        print()
        while not is_fct_known in ['Y', 'n']:
            print('Answer with Y (yes) or n (no) !')
            is_fct_known = input('Do you know the function used (y ≡ ax + b (mod 26) )? [Y/n]:  ')
            print()
            
        # function known
        if is_fct_known == 'Y':
            try:
                a = input('Enter coefficient a: ')
                b = input('Enter ordinate b:    ')
                a = int(a)
                b = int(b)
            except:
                print('Answer with integer numbers!')
                a = input('Enter coefficient a: ')
                b = input('Enter ordinate b:    ')     
                
            # decrypt the message knowing the coefficient and ordinate    
            decryption_pos = affine_encryption_wfct(a, b, encrypted_msg)
            # display the decrypted message knowing a and b
            display_single_pos_ae(decryption_pos)          
                
        else:
            res = affine_encryption(encrypted_msg)
            decryption_pos = res[0]
            a = res[1]
            b = res[2]
            
            display_pos_ae(a, b, decryption_pos)
    




    # POSSIBILITIES STORAGE
    
    print()
    stock_outpout = input('Do you want to stock the outpout in a text file [Y/n]:   ')
    while not stock_outpout in ['Y', 'n']:
        print()
        print('Please answer with correctly!')
        stock_outpout = input('Do you want to stock the outpout in a text file [Y/n]:   ')

    if stock_outpout == 'Y':
        print()
        file_name = input('How would you name the file? ')
        print()
        file = save_to_file(decryption_pos, file_name)
        print(f'File created: {file}.txt')
        print()
        print('End of the programme')
        print()
        print('Close and run the programme to decrypt another message!')
        print()
        
    else:
        print()
        print('End of the programme')
        print()
        print('Close and run the programme to decrypt another message!')
        print()




if __name__ == '__main__':
    interactive_console()
    
    