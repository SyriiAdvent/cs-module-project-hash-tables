import os
dirpath = os.path.dirname(os.path.abspath(__file__))

with open(dirpath + "/ciphertext.txt") as f:
    message = f.read()

secret_key = ['E', 'T', 'A', 'O', 'H',
  'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
  'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K',
  'V', 'Q', 'J', 'X', 'Z'
]

# 'â': 3, '1'

def make_cipher_key(message, secret_key):
  code = {}
  scrambled_egg = [char for char in message if any(c.isalnum() for c in char) and any(c.isalnum() for c in char) and char != 'â' and char != '1']
  for letter in scrambled_egg:
    if letter in code:
      code[letter] += 1
    else:
      code[letter] = 1
  key = {k: v for k, v in sorted(code.items(), key=lambda x: x[1], reverse=True)}
  # print(f'sorted cache: {key}')
  n = 0
  for k in key:
    if n <= len(secret_key) - 1:
      key[k] = secret_key[n]
    n += 1
  return key

# if letter is in cipher, return the value
def letter_decypher(letter):
  if letter.upper() in code:
    return code.get(letter)
  else:
    return letter

# 
def word_parser(s):
  return ''.join([letter_decypher(char) for char in s])

def decrypt(string_code):
  clean_msg = []
  for word in string_code.split():
    clean_msg.append(word_parser(word))
  # print(clean_msg)
  return ' '.join(clean_msg)

code = make_cipher_key(message, secret_key)
print(f'{code} \n\n {decrypt(message)}')

with open(dirpath + "/cracked.txt", mode='w') as f:
    f.write(decrypt(message))