import pyfiglet # type: ignore


# GLOBAL VARIABLES
encrypted_msg = ''
algorithm = ''
algorithms = ['Caesar Cipher', 'Affine Encryption', 'Permutation', 'Vigenere Key']

# 1. Caesar Cipher variables: y ≡ x + gap   (mod 26)
gap = None

# 2. Affine Encyption variables: y ≡ ax + b (mod 26)
a = None
b = None 

# 3. Permutation: y -> y'
s = [[], []]

# 4. Vigenere key: y = x + key[i]
key = ''


# BASIC FUNCTIONS
def rm_spaces(msg):
    return msg.replace(" ", "")



def interactive_console():
    # print the title
    title  = pyfiglet.figlet_format('CryptoAnalyst')
    print(title)
    
    # display menu
    print()
    encrypted_msg = input('Enter the message to decrypt')

if __name__ == '__main__':
    interactive_console()