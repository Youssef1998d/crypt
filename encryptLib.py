import tink
from tink import KeysetHandle, daead, cleartext_keyset_handle
from keyset_tink import read_keyset


daead.register()
keyset_handle = read_keyset("keyset.json")
daead_primitive = keyset_handle.primitive(daead.DeterministicAead)
ASSOCIATED_DATA = b"associated data"

database = 'database.txt'

import bcrypt

def hash_password(pwd, salt = None):
  if salt is None:
    salt = bcrypt.gensalt()
  return bcrypt.hashpw(pwd.encode(), salt), salt

def encrypt(input):
  return daead_primitive.encrypt_deterministically(input, ASSOCIATED_DATA) #AES

def save(uname, pwd):
  hashed_password, salt = hash_password(pwd)
  encrypted_password = encrypt(hashed_password)
  with open(database, 'a') as f:
    f.write(f'{uname},{encrypted_password.hex()},{salt.hex()}\n')

def searchNCheck(user, pwd):
  with open(database, 'r') as f:
    for line in f.readlines():
      user_found, encrypted_password, salt = line.split(',')
      if user == user_found:
        hashed_password = hash_password(pwd, bytes.fromhex(salt))[0]
        encrypted_user_password = encrypt(hashed_password)
        return encrypted_user_password == bytes.fromhex(encrypted_password)
  return False