import pyfiglet # type: ignore
from caesar_cipher import caesar_cipher, caesar_cipher_wgap

# GLOBAL VARIABLES
encrypted_msg = ''
algorithm = ''
algorithms = ['Caesar Cipher', 'Affine Encryption', 'Permutation', 'Vigenere Key']
decryption_pos = []

# 1. Caesar Cipher variables: y ≡ x + gap   (mod 26)
gap = None
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

def display_pos(posibilities):
    pass
    
def display_single_pos(possibility):
    print()
    print('Analyse.')
    print('Analyse..')
    print('Analyse...')
    print()
    print(f'Decrypted message:  {possibility}')
    print()




def interactive_console():
    # print the title
    title  = pyfiglet.figlet_format('CryptoAnalyst')
    print(title)
    print()
    print('ENCRYPTION ALGORITHMS:')
    print('- Caesar Cipher      (1)')
    print('- Affine Encryption  (2)')
    print('- Permutation        (3)')
    print('- Vigenere Key       (4)')
    
    # display menu
    print()
    try:
        encrypted_msg = input('Enter the message to decrypt:    ')
        encrypted_msg = str(encrypted_msg)
        encrypted_msg = rm_spaces(encrypted_msg)
    except:
        print("Do not enter special character, they are not supported yet!")
        
    print()
    
    algorithm = input('Choose the algorithm you think was used to encrypt this message: ')
    while algorithm not in algorithms and algorithm not in ['1', '2', '3', '4']:
        print()
        print('Enter only one of the supported algorithm!')
        print()
        algorithm = input('Choose the algorithm you think was used to encrypt this message: ')
        
    print()
    # Caesar Cipher decryption
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
                gap = input('Enter the gap used: ')
                
            decryption_pos = caesar_cipher_wgap(gap, encrypted_msg) 
            
            display_single_pos(decryption_pos)

        # Gap Unknown
        else:
            decryption_pos = caesar_cipher(encrypted_msg) 
            
            display_pos(decryption_pos)






if __name__ == '__main__':
    interactive_console()