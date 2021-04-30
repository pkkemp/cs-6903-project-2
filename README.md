#Insert Project Name Here 

## Installation 

This program runs on python 3.0 or greater 

## Usage 

```
python main.py
```

## Overview

This decision tree was created to help users best identify whether a Partially Homomorphic Encryption System was right for them. By answering a few short questions, our project can suggest a scheme that is best suited for the task at hand. 

## Understanding the Output

The project considers a total of 7 different schemes before selecting the best option for the user. 

Partially Homomorphic Encryption (PHE) systems are notable for supporting a limited number of mathematical operations over encrypted data. This is helpful because that means the data does not have to be decrypted to plaintext format in order for calculations to be done, allowing for anonymity of data that may contain personally identifiable information otherwise, amongst other use cases. 

### Textbook RSA 
Textbook RSA works with respect to calculations involving Products only. It is a fairly efficient scheme however, it is not the most secure. 

Textbook RSA is perhaps the least secure option on the list but that doesn't mean it doesn't have a purpose. RSA works for both encryption and also a signature function. This implementation for PHE systems does not support padding, which is a key factor in making RSA secure. 

### El Gamal 
This encryption scheme is based on the Diffie-Hellman key exchange, and designed in 1985. 

El Gamal works with respect to Product as well. While this scheme is slower than Textbook RSA for purposes of encryption, it has about the same efficiency for decryption. This scheme is also much more secure than Textbook RSA. 

Modern use cases of this example include PGP as well as the Digital Signature Algorithm scheme. 

### Goldwasser-Micali 
Goldwasser-Micali encryption scheme is a probabilistic encryption scheme developed in 1982. It was proven to be secure, however it results in encrypted text that can be many times longer than the plaintext input. This limitation may make the scheme impractical for many use cases.  

This scheme is homomorphic with respect to XOR operations over the dataset. 

### Rabin
Rabin encryption scheme was developed in 1979 by Michal O. Rabin as the first asymetric cryptosystem. Recovering plaintext for a Rabin encrypted ciphertext is proven to be as hard as factoring. This scheme is faster than RSA for encryption purposes, but about the same efficiency for decryption. 

Rabin is homomorphic with respect to both Product and XOR operations. 

### Paillier 
The Paillier encryption scheme was developed in 1999 by Pascal Paillier. Like Rabin, this is also an asymetric algorithm. This scheme is homomorphic with respect to Sum operations.

Practical usage of this scheme include electronic voting by protecting the privacy of voters while allowing accurate counting of results. Another use case is electronic cash which allows a vendor to charge a credit card using an encrypted version of it. This retains the privacy and identity of the cardholder/buyer. 

### Benaloh 
The Benaloh system was created in 1985 by Josh benaloh. This system is an improvement on the GOldwasser Micali cryptosystem because it encrypts larger blocks of data at once instead of going bit by bit. Like Goldwasser Micali this scheme is homomorphic on XOR operations. 
In terms of efficiency, this scheme is considered to be faster than Goldwasser Micali due to its larger block encryption size. 

### Damgard-Jurkin 
The Damgard Jurik cryptosystem is a spin off of the Paillier system. It is homomorphic with regards to Sum and is faster than Paillier in some cases. 