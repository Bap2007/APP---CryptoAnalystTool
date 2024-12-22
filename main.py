import pyfiglet # type: ignore
import os
from caesar_cipher import caesar_cipher, caesar_cipher_wgap

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

def display_pos(posibilities, gaps):
    print()
    print('Possible Answers: ')
    print()
    for i in range(len(posibilities)):
        print(f'outpout: {posibilities[i]}    gap: {gaps[i]}\n')
    print()
        
def display_single_pos(possibility):
    print()
    print('Analyse.')
    print('Analyse..')
    print('Analyse...')
    print()
    print(f'Decrypted message:  {possibility}')
    print()


def save_to_file(data_list, name):
    os.makedirs('data', exist_ok=True)
    file_path = os.path.join('data', f'pos{name}')
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:

            file.write(item + '\n')
            
    return file_path


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
            res = caesar_cipher(encrypted_msg) 
            decryption_pos = res[0]
            cor_gaps = res[1]
            
            display_pos(decryption_pos, cor_gaps)





        # Option to stock the possibilities in a text file
        print()
        stock_outpout = input('Do you want to stock the outpout in a text file [Y/n]')
        while not stock_outpout in ['Y', 'n']:
            print()
            print('Please answer with correctly!')
            stock_outpout = input('Do you want to stock the outpout in a text file [Y/n]')

        if stock_outpout == 'Y':
            print()
            file_name = input('How would you name the file? ')
            print()
            file = save_to_file(decryption_pos, file_name)
            print(f'File created: {file}')
            
        else:
            print()
            print('End of the programme')
            print()
            print('Close and run the programme to decrypt another message!')
            print()




if __name__ == '__main__':
    interactive_console()
    
    