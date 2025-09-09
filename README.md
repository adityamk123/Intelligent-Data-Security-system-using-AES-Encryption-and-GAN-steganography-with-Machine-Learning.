# Intelligent-Data-Security-system-using-AES-Encryption-and-GAN-steganography-with-Machine-Learning.

## Project Overview

This project demonstrates a secure data hiding system that combines AES encryption, Generative Adversarial Networks (GANs) for realistic image generation, and Least Significant Bit (LSB) steganography for embedding secret messages inside AI-generated images. Finally, a Streamlit-based GUI is built to make the system interactive and user-friendly.

## Key Idea:

Encrypt the message using AES.

Generate a realistic image using Stable Diffusion (GAN-based).

Embed the encrypted message inside the generated image using LSB steganography.

Extract & decrypt the hidden message from the image.

Provide an easy-to-use GUI for demonstration.

## Features

AES Encryption: Ensures message confidentiality before embedding.

GAN-based Image Generation: Generates realistic cover images dynamically.

LSB Steganography: Securely hides data at the pixel level.

AES Decryption: Retrieves the original hidden message.

Streamlit GUI: Simple and intuitive user interface for live demo.

## Project Architecture
```
User Input → AES Encryption → GAN Image Generation → LSB Encoding → Encoded Image  
Encoded Image → LSB Decoding → AES Decryption → Original Message
```
## Project Structure
```
SecureGAN_Stegano/
│
├── main.py                # Command-line execution (without GUI)
├── app.py                 # Streamlit GUI app
│
├── security/
│   └── aes_crypto.py      # AES encryption & decryption
│
├── models/
│   └── gan_model.py       # GAN/Stable Diffusion image generator
│
├── steganography/
│   └── lsb.py             # LSB encoding & decoding functions
│
├── encoded.png            # Output image with hidden message (generated at runtime)
├── generated.png          # Raw GAN-generated image (optional)
│
└── requirements.txt       # Required dependencies
```
## How It Works
```
Encryption: User enters a secret message → encrypted using AES before hiding.

Image Generation: GAN / Stable Diffusion generates a new cover image from a text prompt.

Steganography: Encrypted message is embedded into the generated image via LSB manipulation.

Decoding: Hidden bits are extracted → AES decryption restores the original message.
```
## Streamlit GUI

The Streamlit app (app.py) provides:

Input fields for secret message & text prompt.

Automatic encryption, image generation, and message embedding.

Display of original message → encrypted message → decoded & decrypted message.

Visualization of generated and encoded images.

## Technologies Used
```
Python 3.x

PyCryptodome (AES encryption)

Diffusers / Stable Diffusion (GAN-based image generation)

NumPy & Pillow (Image processing)

Streamlit (GUI)
```
## Future Scope

Implement advanced steganography methods (DCT, DWT).

Add user-defined AES keys.

Extend GUI with upload image & extract mode.

Enhance GAN model for more realistic outputs.
