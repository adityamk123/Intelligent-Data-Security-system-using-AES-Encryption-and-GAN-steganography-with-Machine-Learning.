import streamlit as st
from security.aes_crypto import AESCipher
from models.gan_model import generate_image
from steganography.lsb import encode_image, decode_image
from PIL import Image

st.title("🔐 SecureGAN Steganography Demo")

# User input
message = st.text_input("Enter your secret message:")

if st.button("Generate & Encode"):
    if message.strip() != "":
        st.write("Original message:", message)

        # Encrypt
        cipher = AESCipher()
        encrypted = cipher.encrypt(message)
        st.write("Encrypted:", encrypted)

        # Generate AI Image
        prompt = "A futuristic cyber cityscape, ultra detailed, 4k"
        img = generate_image(prompt)

        # Encode
        encode_image(img, encrypted, "encoded.png")
        st.success("Message hidden inside encoded.png")

        # Show images
        st.image(img, caption="Generated Image", use_container_width=True)
        st.image("encoded.png", caption="Encoded Image with hidden data", use_container_width=True)

        # Decode + Decrypt
        extracted = decode_image("encoded.png", len(encrypted))
        decrypted = cipher.decrypt(extracted)
        st.write("🔓 Decrypted Message:", decrypted)
    else:
        st.warning("Please enter a message!")
