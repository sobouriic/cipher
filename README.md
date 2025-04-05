# Caesar Cipher Encryption and Decryption

This project implements the **Caesar Cipher**, to understand basic concepts of cryptography,and how simple ciphers work, particularly focusing on the Caesar Cipher algorithm .a simple encryption algorithm that shifts letters in the alphabet by a fixed number.

## Table of Contents
1. [Introduction](#introduction)
2. [How It Works](#how-it-works)
3. [Algorithm](#algorithm)
4. [Features](#features)
5. [Usage](#usage)
6. [Where Can You Use It?](#where-can-you-use-it)
7. [Testing](#testing)

---

## Introduction

The Caesar Cipher is one of the oldest and simplest encryption techniques. It was named after Julius Caesar, who used it to protect his private messages. The cipher works by shifting each letter of the message by a fixed number, called the "shift." For example, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on.

This implementation allows you to:
- Encrypt a message using a Caesar shift.
- Decrypt an encrypted message back to its original form.
- Handle non-alphabetic characters such as spaces, punctuation, and numbers.
---

## How It Works

### Encryption:
1. Take a plaintext message (e.g., "Hello World!").
2. Choose a shift value (e.g., `3`).
3. Each letter of the message is shifted by the shift value. For example, `H` becomes `K`, `E` becomes `H`, etc.
4. Non-alphabetic characters (e.g., spaces, punctuation) are not altered.
5. Return the encrypted message.

### Decryption:
1. Take the encrypted message.
2. Use the same shift value (e.g., `3`) to shift each letter **backwards** to retrieve the original message.
3. Non-alphabetic characters remain unchanged.
4. Return the decrypted message.

---

## Algorithm

The **Caesar Cipher** algorithm follows these simple steps:

1. **Initialize**: Choose a shift value `n` (e.g., `n = 3`).
2. **Encryption**: For each character in the message:
   - If the character is a letter (A-Z or a-z), shift it by `n` positions in the alphabet.
   - If the character is not a letter (e.g., spaces, punctuation), leave it unchanged.
3. **Decryption**: For each character in the encrypted message:
   - If the character is a letter (A-Z or a-z), shift it back by `n` positions in the alphabet.
   - If the character is not a letter, leave it unchanged.
4. **Output**: The encrypted or decrypted message.

---

## Features

- **Encrypt and Decrypt**: Encrypt and decrypt messages with a customizable shift value.
- **Handles Non-Alphabetic Characters**: Spaces, punctuation, and numbers are preserved in both encryption and decryption.
- **Large Shifts**: The cipher can handle shifts larger than 26 by wrapping around the alphabet.

---

## Usage

### Installing the project
1. **Clone this repository** to your local machine:
   ```bash
   git clone 
   cd cipher-encryption
2. **Set up a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
3. **Running Tests:**
    ```bash
    python -m unittest discover tests/

