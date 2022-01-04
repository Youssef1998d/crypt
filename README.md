# crypt

Subject : (https://vqhuy.github.io/teaching/crypto/td5).

## Usage of the scripts

install all dependencies.

```bash
pip install -r dependencies.txt 
```

 `keyset.json` file can be used or creating a new one by running the `keyset_tink.py` script is also a solution. 

 by running `main.py` script, graphical interaction will take place in order to register or to login.

## strength of a password?

### **Question 1**: What is minimum length of a password created from case-insensitive alphanumeric and having 64-bit of entropy?

the password has to be minimum 13 characters (12.37928983150533).

## How to securely store user passwords?

### Naive approach

The naive approach would be to store the password as hash like sha 1, 2, ...

```py
hash = sha3(password)
store(hash)
```

### Increasing the entropy

We need to add salt before the hash. Then, a hacker can only brute force password 1 by 1.

```py
salt = os.urandom(32)
hash = scrypt(salt + password)
store(salt, hash)
```

### Which hashing algorithm to use

scrypt, bcrypt, argon2

### Data breaches and how to deal with it

Have asymmetric encryption with a secret key. As we have only one secret key for our whole app, it is easier to secure.

```py
salt = os.urandom(32)
hash = scrypt(salt + password)
# Deterministic encryption
encrypted_hash = encryption_machine(hash)
store(salt, encrypted_hash)
```
Youssef Drira. 
